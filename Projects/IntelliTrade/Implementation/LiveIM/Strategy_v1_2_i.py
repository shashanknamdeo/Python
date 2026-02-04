"""
Strategy: ADX-DMI-HT-Inverted

Implementation Details:
-> Implemented Inverted Strategy. Inversion of BTstrategyADXDMIHT_v1_2_i
-> Selling CE(during INITIATE_LONG) and PE(during INITIATE_SHORT) Options.

"""

import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import math
import json
import time
import pause
import urllib3
import pandas as pd
from textwrap import wrap
from pprint import pprint
from functools import reduce
from datetime import datetime
from datetime import timedelta
from tabulate import tabulate

import threading
from threading import Event
from threading import Condition

import SysPath
from Logging import initializeLogger

from LibWriteToFile import writeTextToFile

from LibNSEUtils import getExpiryDateOfATradeDate

from LibLogin import TradeLogin

from GlobalVariables import MODULE_SOUND_DIR
from GlobalVariables import INSTRUMENT_LOT_SIZE_DICT
from GlobalVariables import GOOGLEDRIVE_TRADE_SYNC_DATA_DIR
from GlobalVariables import INSTRUMENT_STRIKE_PRICE_STEP_SIZE_DICT
from GlobalVariables import GOOGLEDRIVE_TRADE_LOGS_DIR

from GlobalFunctions import printTabulateDataFrame

from LibIndicators import indicatorDMI
from LibIndicators import indicatorADX
from LibIndicators import indicatorHalfTrend

from LibPlayAudioFromFile import playAudioFromWavFile_v1

import LibOrderManagement
from LibOrderManagement import cancelOrder
from LibOrderManagement import createOrderDict
from LibOrderManagement import processOrder
from LibOrderManagement import processStoplossOrder
from LibOrderManagement import processTargetOrder
from LibOrderManagement import populateOrderManagementDFStatus
from LibOrderManagement import getExecutionPriceFromOrderReport
from LibOrderManagement import getExecutionStatusFromOrderReport
from LibOrderManagement import populateOrderManagementDFWithExecutionPrice

from LibInstruments import getInstrumentFNOTokens
from LibInstruments import getInstrumentIndexToken
from LibInstruments import fetchAndSaveInstrumentFNOTokens

from FetchHistoricalData import fetchHistoricalDataParameterized
from FetchHistoricalData import fetchHistoricalDataFNOParameterized

from LoadIndexHistoricalData import convertIndexDataFrameTimeInterval
from LoadIndexHistoricalData import convertStringIntervalToIntMinutes

from LiveTradeUtilities import raiseNetworkError
from LiveTradeUtilities import fetchInstrumentLTP
from LiveTradeUtilities import fetchInstrumentLTPFromInstrumentToken

# ----------------------------------------------------------------------------------------------------------------------

global logger
global client
global instrumentDF
global parameter_dict
global active_trade_dict_CE
global active_trade_dict_PE
global active_trade_status_CE
global active_trade_status_PE

active_trade_dict = None
active_trade_status = 0

instrumentDF = pd.DataFrame()

# ----------------------------------------------------------------------------------------------------------------------
# Improvement: To load at specific-time. example: 10:50:10 [To guarantee new data to be available to 
# other consuming processes]. Else, find a way to tell other threads/functions.


# Enriching-Data-For-Strategy
def enrichInstrumentDataWithIndicators(instrument_interval_dict):
    """
    Make this function more generic to implement dynamic indicators addition. [Accept list/dict of indicators]
    """
    instrumentDF = instrument_interval_dict[parameter_dict['interval']]
    indicator_dict = parameter_dict['indicator_dict']
    # 
    dmiDF = indicatorDMI(hlc_df=instrument_interval_dict[indicator_dict['indicatorDMI']['interval']], lookback=indicator_dict['indicatorDMI']['lookback'], version=indicator_dict['indicatorDMI']['version'])
    adxDF = indicatorADX(hlc_df=instrument_interval_dict[indicator_dict['indicatorADX']['interval']], lookback=indicator_dict['indicatorADX']['lookback'], version=indicator_dict['indicatorADX']['version'])
    halfTrendDF  = indicatorHalfTrend(hlc_df=instrument_interval_dict[indicator_dict['indicatorHalfTrend']['interval']], version=indicator_dict['indicatorHalfTrend']['version'])
    instrumentDF = reduce(lambda df1, df2 : pd.merge(df1, df2, left_on='trade_datetime', right_on='trade_datetime', how='left'), [instrumentDF, dmiDF, adxDF, halfTrendDF])
    instrumentDF.ffill(inplace=True)
    # 
    return instrumentDF


# Fetching--Data
def fetchDataTimeFrameList():
    """
    fetchDataTimeFrameList(interval_list=['5MINUTE', '15MINUTE'])
    fetchHistoricalDataParameterized(instrument_name='NIFTYBANK', start_date='20231001', end_date='20231013', interval='5MINUTE')
    fetchHistoricalDataParameterized(instrument_name='NIFTYBANK', start_date=start_date, end_date=end_date, interval='15MINUTE')
    """
    global instrumentDF
    start_date     = (datetime.strptime(parameter_dict['trade_date'], '%Y%m%d') - timedelta(days=20)).strftime('%Y%m%d')
    end_date       = parameter_dict['trade_date']
    indicator_dict = parameter_dict['indicator_dict']
    interval_list  = list(set([indicator_dict[item]['interval'] for item in indicator_dict]))
    instrument_interval_dict = {}
    # 
    try:
        instrumentDF_MINUTE = fetchHistoricalDataParameterized(instrument_name=parameter_dict['instrument_name'], start_date=start_date, end_date=end_date, interval='MINUTE')
        for interval in interval_list:
            instrument_interval_dict[interval] = convertIndexDataFrameTimeInterval(instrumentDF=instrumentDF_MINUTE, interval=interval)
        instrumentDF = enrichInstrumentDataWithIndicators(instrument_interval_dict)
        return True
    except Exception as e:
        logger.exception(e)
        raise(e)

# ----------------------------------------------------------------------------------------------------------------------
# Strategy-Implementation

def getExecutionPriceFromOrderReportUntilTraded(order_id, loop_sleep_duration=0.5):
    """
    Function to keep checking for the order to be traded and return execution price post TARD.
    *Caution -> Will block the execution till return.
    """
    while True:
        execution_status, order_row = getExecutionStatusFromOrderReport(client=client, logger=logger, order_id=order_id)
        if execution_status == 'TRAD':
            execution_price = order_row['price']
            return execution_price
        time.sleep(loop_sleep_duration)


def initiateOptionMarketOrderTradeWtihStopLossTarget(option_type, strike_price, transaction_type, quantity):
    """
    """
    global parameter_dict
    # 
    trade_date        = parameter_dict['trade_date']
    instrument_name   = parameter_dict['instrument_name']
    expiry_week_ahead = parameter_dict['expiry_week_ahead']
    stoploss_percent  = parameter_dict['stoploss_percent']
    # 
    expiry_date       = getExpiryDateOfATradeDate(instrument_name=instrument_name, date=trade_date, week_ahead=expiry_week_ahead)
    option_token      = getInstrumentFNOTokens(instrument_name=instrument_name, expiry_date=expiry_date, strike_price=strike_price, option_type=option_type)
    # 
    order_dict = {
        'strategy_name'   : parameter_dict['strategy_name'], 
        'instrument_name' : instrument_name,
        'instrument_token': option_token,
        'instrument_type' : 'OPTION',
        'option_type'     : option_type,
        'strike_price'    : strike_price,
        'expiry_date'     : expiry_date,
        'transaction_type': transaction_type,
        'quantity'        : quantity,
        'price'           : 0, # Market-Order
        'order_type'      : 'N',
        'order_timestamp' : datetime.now().strftime('%Y%m%d_%H%M%S'),
    }
    logger.info(order_dict)
    # 
    order_id = processOrder(client=client, order_dict=order_dict, logger=logger)
    if order_id:
        order_dict['transaction_order_id'] = order_id
        order_dict['transaction_order_status'] = 'OPEN'
    elif order_id is None:
        playAudioFromWavFile_v1(os.path.join(MODULE_SOUND_DIR, 'Data', 'Emergency', 'Emergency01.wav'))
        raise('Order-Execution-Failed')
    # 
    execution_price = getExecutionPriceFromOrderReportUntilTraded(order_id=order_id)
    order_dict['stoploss_price']  = round(execution_price*(1 + parameter_dict['stoploss_percent']*0.01), 1)
    order_dict['target_price']    = round(execution_price*(1 - parameter_dict['target_percent']*0.01), 1)
    # 
    stoploss_order_id = processStoplossOrder(client=client, order_dict=order_dict, logger=logger)
    if stoploss_order_id:
        order_dict['stoploss_order_id'] = stoploss_order_id
        order_dict['stoploss_order_status'] = 'SLO'
    else:
        playAudioFromWavFile_v1(os.path.join(MODULE_SOUND_DIR, 'Data', 'Emergency', 'Emergency01.wav'))
        raise('StopLoss-Order-Execution-Failed')
        # return {}
    # 
    target_order_id = processTargetOrder(client=client, logger=logger, order_dict=order_dict)
    if target_order_id:
        order_dict['target_order_id'] = target_order_id
        order_dict['target_order_status'] = 'OPEN'
    else:
        playAudioFromWavFile_v1(os.path.join(MODULE_SOUND_DIR, 'Data', 'Emergency', 'Emergency01.wav'))
        raise('Target-Order-Execution-Failed')
    # 
    return order_dict


def exitMarketOrderTrade():
    """
    Another implementation method is to cancle the stoploss trade and completing the target order at
    the current ltp.
    
    Implementation just negating transaction_type. All parameters remains same
    """
    if active_trade_dict is not None:
        order_dict = active_trade_dict['order_dict']
        stoploss_order_id = order_dict['stoploss_order_id']
        target_order_id = order_dict['target_order_id']
        stoploss_status = getExecutionStatusFromOrderReport(client=client, logger=logger, order_id=stoploss_order_id)
        target_status = getExecutionStatusFromOrderReport(client=client, logger=logger, order_id=target_order_id)
        # 
        if stoploss_status == 'TRAD' and target_status == 'OPN':
            cancelOrder(client=client, logger=logger, order_id=target_order_id)
        # 
        elif stoploss_status == 'OPN' and target_status == 'TRAD':
            cancelOrder(client=client, logger=logger, order_id=stoploss_order_id)
        # 
        elif stoploss_status == 'OPN' and target_status == 'OPN':
            cancelOrder(client=client, logger=logger, order_id=stoploss_order_id)
            cancelOrder(client=client, logger=logger, order_id=target_order_id)
            # 
            exit_order_dict = {}
            exit_order_dict['instrument_token'] = order_dict['instrument_token']
            exit_order_dict['order_type'] = order_dict['order_type']
            exit_order_dict['transaction_type'] = 'BUY' if order_dict['transaction_type'] == 'SELL' else 'SELL'
            exit_order_dict['quantity'] = order_dict['quantity']
            exit_order_dict['price'] = 0
            logger.debug('exit_order_dict: {}'.format(exit_order_dict))
            order_id = processOrder(client=client, order_dict=exit_order_dict, logger=logger)
        else:
            logger.debug('No-Matching-Condition')
            raise Exception('No-Matching-Condition')
    else:
        logger.debug('active_trade_dict Already-None')
    return None


def calculateActiveTradeStatus(active_trade_dict):
    """
    Temporary function to find the active_trade_status from active_trade_dict.
    Need to find a better way to mange active trades and its notifications.
    """
    if active_trade_dict and active_trade_dict['transaction_status'] == 'OPEN' and active_trade_dict['option_type'] == 'CE':
        return 1
    elif active_trade_dict and active_trade_dict['transaction_status'] == 'OPEN' and active_trade_dict['option_type'] == 'PE':
        return -1
    else:
        return 0


def createCheckADXDMIHTConditionDict(row, parameter_dict):
    """
    """
    _dict = {
        'plus_di'    : row['plus_di'],
        'minus_di'   : row['minus_di'],
        'adx'        : row['adx'],
        'halftrend'  : row['halftrend'],
        'adx_threshold_pre_trade'        : parameter_dict['threshold_dict']['adx_threshold_pre_trade'],
        'adx_threshold_post_trade'       : parameter_dict['threshold_dict']['adx_threshold_post_trade'],
        'plus_di_minus_di_required_diff' : parameter_dict['threshold_dict']['plus_di_minus_di_required_diff'],
        'plus_di_threshold_pre_trade'    : parameter_dict['threshold_dict']['plus_di_threshold_pre_trade'],
        'plus_di_threshold_post_trade'   : parameter_dict['threshold_dict']['plus_di_threshold_post_trade'],
        'minus_di_threshold_pre_trade'   : parameter_dict['threshold_dict']['minus_di_threshold_pre_trade'],
        'minus_di_threshold_post_trade'  : parameter_dict['threshold_dict']['minus_di_threshold_post_trade']
    }
    return _dict


def checkADXDMIHTCondition_v3(active_trade_status, halftrend, plus_di, minus_di, adx, adx_threshold_pre_trade, adx_threshold_post_trade, plus_di_minus_di_required_diff, plus_di_threshold_pre_trade, plus_di_threshold_post_trade, minus_di_threshold_pre_trade, minus_di_threshold_post_trade):
    """
    active_trade_status : 0(if no active trade). 
                          LONG(+1)/SHORT(-1)](if either in long or in short active trade)
    
    Return Values:
        DO_NOTHING     ->  0
        INITIATE_LONG  -> +1
        INITIATE_SHORT -> -1
        INITIATE_EXIT  ->  None
    
    Try-1 if halftrend condition is ommited.
    Try-2 if DMI condition is ommited.
    Try-3 if ADX condition is ommited.
    """
    if active_trade_status == 0:
        if (halftrend == +1) and (adx > adx_threshold_pre_trade) and (plus_di > plus_di_threshold_pre_trade):
            return +1 # 'INITIATE_LONG'
        elif (halftrend == -1) and (adx > adx_threshold_pre_trade) and (minus_di > minus_di_threshold_pre_trade):
            return -1 # 'INITIATE_SHORT'
        else:
            return  0 # 'DO_NOTHING'
    # 
    elif active_trade_status:
        return 0 # 'DO_NOTHING'


def createActiveTradeDict(order_dict, strike_price, quantity):
    """
    """
    # 
    active_trade_dict = {}
    active_trade_dict['strike_price']      = strike_price
    active_trade_dict['quantity']          = quantity
    active_trade_dict['order_dict']        = order_dict
    return active_trade_dict


def strategyADXDMIHT_v1_2_i():
    """
    Implementation: Long/Short trade initiation/exit is executed at the intervals (eg. 5MINUTES)
    """
    global active_trade_status
    global active_trade_dict
    global parameter_dict
    global instrumentDF
    # 
    instrument_name        = parameter_dict['instrument_name']
    step_size              = parameter_dict['step_size']
    lot_quantity           = parameter_dict['lot_quantity']
    strike_price_bandwidth = parameter_dict['strike_price_bandwidth']
    # 
    row = instrumentDF.iloc[-1]
    response = checkADXDMIHTCondition_v3(active_trade_status=active_trade_status, **createCheckADXDMIHTConditionDict(row=row, parameter_dict=parameter_dict))
    logger.debug('| trade_datetime: {} | open: {:7.2f} | high: {:7.2f} | low: {:7.2f} | close: {:7.2f} | plus_di: {:5.2f} | minus_di: {:5.2f} | adx: {:5.2f} | halftrend: {:+} | active_trade_status: {} | response: {} |' \
        .format(row.trade_datetime, row.open, row.high, row.low, row.close, row.plus_di, row.minus_di, row.adx, row.halftrend, active_trade_status, response))
    # 
    if response == 0:
        pass # DO_NOTHING
    # 
    elif response == +1:
        # INITIATE [CE_SHORT]
        logger.info('INITIATE_CE_SHORT_POSITION | row: {}'.format(row.to_dict()))
        instrument_ltp            = row.close
        bandwidth_factor          = +1
        roundoff_instrument_price = round(int(instrument_ltp)/step_size)*step_size
        strike_price              = roundoff_instrument_price + strike_price_bandwidth*bandwidth_factor
        quantity                  = int(lot_quantity*INSTRUMENT_LOT_SIZE_DICT[instrument_name])
        order_dict                = initiateOptionMarketOrderTradeWtihStopLossTarget(strike_price=strike_price, option_type='CE', transaction_type='SELL', quantity=quantity)
        active_trade_dict         = createActiveTradeDict(order_dict=order_dict, strike_price=strike_price, quantity=quantity)
        active_trade_status       = calculateActiveTradeStatus(order_dict)
        saveTradeStatusToDisk()
        playAudioFromWavFile_v1(os.path.join(MODULE_SOUND_DIR, 'Data', 'Notification', 'Notification03.wav'))
        return True
    elif response == -1:
        # INITIATE [PE_SHORT]
        logger.info('INITIATE_PE_SHORT_POSITION | row: {}'.format(row.to_dict()))
        instrument_ltp            = row.close
        bandwidth_factor          = -1
        roundoff_instrument_price = round(int(instrument_ltp)/step_size)*step_size
        strike_price              = roundoff_instrument_price + strike_price_bandwidth*bandwidth_factor
        quantity                  = int(lot_quantity*INSTRUMENT_LOT_SIZE_DICT[instrument_name])
        order_dict                = initiateOptionMarketOrderTradeWtihStopLossTarget(strike_price=strike_price, option_type='PE', transaction_type='SELL', quantity=quantity)
        active_trade_dict         = createActiveTradeDict(order_dict=order_dict, strike_price=strike_price, quantity=quantity)
        active_trade_status       = calculateActiveTradeStatus(order_dict)
        saveTradeStatusToDisk()
        playAudioFromWavFile_v1(os.path.join(MODULE_SOUND_DIR, 'Data', 'Notification', 'Notification03.wav'))
        return True
    # 
    # Check-Stoploss-Target-Hit
    if active_trade_status:
        stoploss_execution_status, _ = getExecutionStatusFromOrderReport(client=client, logger=logger, order_id=active_trade_dict['order_dict']['stoploss_order_id'])
        target_execution_status, _ = getExecutionStatusFromOrderReport(client=client, logger=logger, order_id=active_trade_dict['order_dict']['target_order_id'])
        logger.debug('stoploss_execution_status: {} | target_execution_status: {}'.format(stoploss_execution_status, target_execution_status))
        # 
        if (stoploss_execution_status == 'SLO' and target_execution_status == 'OPN'):
            return
        elif (stoploss_execution_status == 'TRAD' and target_execution_status == 'OPN'):
            cancelOrder(client=client, logger=logger, order_id=active_trade_dict['order_dict']['target_order_id'])
            active_trade_dict = None
            active_trade_status = 0
        elif (stoploss_execution_status == 'SLO' and target_execution_status == 'TRAD'):
            cancelOrder(client=client, logger=logger, order_id=active_trade_dict['order_dict']['stoploss_order_id'])
            active_trade_dict = None
            active_trade_status = 0
        elif (stoploss_execution_status == 'TRAD' and target_execution_status == 'TRAD'):
            raise Exception('BOTH-STOPLOSS-AND-TARGET-ORDER-TRADED')
        else:
            logger.debug('No-Exectuion-Status-Condition-Matched')
    # 



def checkStopLoss():
    """
    """
    global active_trade_dict
    global active_trade_status
    # 
    if active_trade_dict:
        option_token = active_trade_dict['instrument_token']
        option_ltp = fetchInstrumentLTPFromInstrumentToken(instrument_token=option_token)
        # 
        if option_ltp < active_trade_dict['stoploss_price']:
            logger.info('STOPLOSS_HIT | order_dict: {}'.format(active_trade_dict))
            active_trade_dict = exitMarketOrderTrade()
            active_trade_status = 0
            saveTradeStatusToDisk()
            playAudioFromWavFile_v1(os.path.join(MODULE_SOUND_DIR, 'Data', 'Notification', 'Notification03.wav'))


def saveTradeStatusToDisk():
    """
    """
    global active_trade_dict
    global active_trade_status
    json_object = {
        'active_trade_dict': active_trade_dict,
        'active_trade_status': active_trade_status
    }
    logger.debug('json_object: {}'.format(json_object))
    # 
    directory_path = parameter_dict['directory_path']
    with open(os.path.join(directory_path, 'strategyADXDMIHT_v1_2_i_TradeState.json'), 'w+') as output_file:
        json.dump(json_object, output_file, indent=4, sort_keys=True)


def loadTradeStatusFromDisk():
    """
    """
    global active_trade_dict
    global active_trade_status
    # 
    directory_path = parameter_dict['directory_path']
    with open(os.path.join(directory_path, 'strategyADXDMIHT_v1_2_i_TradeState.json'), 'r') as input_file:
        json_object = json.load(input_file)
    # 
    active_trade_dict = json_object['active_trade_dict']
    active_trade_status = json_object['active_trade_status']

# ----------------------------------------------------------------------------------------------------------------------

def initializeMainProcess():
    """
    """
    global logger
    global client
    global parameter_dict 
    # 
    directory_path = os.path.join(GOOGLEDRIVE_TRADE_LOGS_DIR, 'LIVE','LIVE_'+datetime.now().strftime('%Y%m%d'))
    file_name = 'strategyADXDMIHT_v1_2_i'+'_'+datetime.now().strftime('%Y%m%d_%H%M%S')+'.log'
    logger = initializeLogger(directory_path=directory_path, file_name=file_name)
    # 
    indicator_dict = {
        'indicatorDMI'           : {'version': 'v1', 'interval': '5MINUTE', 'lookback': 8,},
        'indicatorADX'           : {'version': 'v1', 'interval': '5MINUTE', 'lookback': 8,},
        'indicatorHalfTrend'     : {'version': 'v2', 'interval': '5MINUTE'},
    }
    parameter_dict = {
        'strategy_name'          : 'strategyADXDMIHT_v1_2_i',
        'instrument_name'        : 'NIFTYBANK',
        'step_size'              : 100,
        'enrichmentFunction'     : 'enrichInstrumentDataWithIndicatorsMP_v2', # Defined in LibEnrichData.
        'expiry_week_ahead'      : 0,
        'strike_price_bandwidth' : 400,
        'lot_quantity'           : 1,
        'trade_start_time'       : '0920',
        'trade_end_time'         : '1520',
        'stoploss_percent'       : 20,
        'target_percent'         : 20,
        'stoploss_price'         : None,
        'target_price'           : None,
        'trailing_stoploss'      : False,
        'target_hit_type'        : 'REALTIME',
        'stoploss_hit_type'      : 'REALTIME',
        'strategy_close'         : False,
        'interval'               : '5MINUTE', # Represent the interval of the algo iteration.
        'indicator_dict'         : indicator_dict,
        'threshold_dict'         : {'adx_threshold_pre_trade': 0, 'adx_threshold_post_trade': 0, 'plus_di_minus_di_required_diff': 0, 'plus_di_threshold_pre_trade': 20, 'plus_di_threshold_post_trade': 0, 'minus_di_threshold_pre_trade': 20, 'minus_di_threshold_post_trade': 0},
        'trade_logs'             : True,
        # 
        'directory_path'         : directory_path,
        'trade_date'             : datetime.now().strftime('%Y%m%d'),
        'trade_start_time'       : '092505',
        'trade_end_time'         : '152505'
    }
    logger.info('parameter_dict: {}'.format((json.dumps(parameter_dict, indent=4))))
    # 
    try:
        client = TradeLogin(username='USER_1')
        logger.debug('Connection-Established')
    except urllib3.exceptions.MaxRetryError as e:
        logger.error(e)
        logger.debug('Check-Network-Connection')
        sys.exit(1)
    # 
    # fetchAndSaveInstrumentFNOTokens() # Implement to download only once a dat at-maximum.
    return True


def processRunTimeContition(process_start_time, processed_end_time):
    """
    processRunTimeContition(process_start_time='110010', processed_end_time='152010')
    """
    if (datetime.now().strftime('%H%M%S') >= process_start_time) and (datetime.now().strftime('%H%M%S') <= processed_end_time):
        return True
    else:
        return False


def updateHeartBeatDataToFile_v2(file_name, pattern, separator=' -> '):
    """
    file_name = os.path.join(GOOGLEDRIVE_TRADE_LOGS_DIR, 'HEARTBEAT_STRATEGY_ADXDMIHT.txt')
    updateHeartBeatDataToFile_v2(file_name=file_name, pattern='strategyADXDMIHT_v1_2_i')
    """
    time_now_yyyymmdd = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    line_to_write = pattern + separator + str(time_now_yyyymmdd)
    writeTextToFile(file_name=file_name, text=line_to_write)


def activeThreadsMonitoring():
    """
    """
    file_path = os.path.join(GOOGLEDRIVE_TRADE_LOGS_DIR, 'LIVE', 'ActiveThreadMonitoring', 'ActiveThreadsName_strategyADXDMIHT_v1_2_i.txt')
    with open(file_path) as f:
        file_thread_names_list = f.read().splitlines()
    # 
    live_thread_names_list = [t.name for t in threading.enumerate()]
    missing_thread_name_list = [thread_name for thread_name in file_thread_names_list if thread_name not in live_thread_names_list and not thread_name.startswith('#')]
    # 
    if missing_thread_name_list == []:
        return None
    else:
        logger.critical('missng_threads: {}'.format(missing_thread_name_list))
        playAudioFromWavFile_v1(os.path.join(MODULE_SOUND_DIR, 'Data', 'Emergency', 'Emergency01.wav'))
        # playAudioFromWavFile_v1(os.path.join(MODULE_SOUND_DIR, 'Data', 'Emergency', 'MotuPandaShaitanBiwiAlert.wav'))


def validateInstrumentData():
    """
    Needs to validate instrument data, that the last row is as recent as possible.
    """
    global instrumentDF
    interval_minutes = convertStringIntervalToIntMinutes(interval_string=parameter_dict['interval'])
    datetime_delay = datetime.now().strftime('%Y%m%d')+'_'+'{:04d}'.format(math.floor(int((datetime.now()-timedelta(minutes=interval_minutes)).strftime('%H%M'))/interval_minutes)*interval_minutes)
    datetime_instrument_last_row = instrumentDF.iloc[-1].trade_datetime
    # logger.debug('datetime_delay: {} | datetime_instrument_last_row: {}'.format(datetime_delay, datetime_instrument_last_row))
    if datetime_instrument_last_row >= datetime_delay:
        return True
    else:
        logger.info('datetime_delay: {} | datetime_instrument_last_row: {}'.format(datetime_delay, datetime_instrument_last_row))
        raise Exception('TimeValidation-Failed')


def strategyADXDMIHT_v1_2_i_Main():
    """
    """
    try:
        fetchDataTimeFrameList()
        validateInstrumentData()
        strategyADXDMIHT_v1_2_i()
    except Exception as e:
        logger.exception(e, exc_info=True, stack_info=False)
        raise e


def generateNextDateTimeWithInterval(start_time_HHMMSS, interval):
    """
    generateNextDateTimeWithInterval(start_time_HHMMSS='110011', interval=300)
    """
    today_datetime = datetime.now()
    _datetime = datetime(today_datetime.year, today_datetime.month, today_datetime.day, int(start_time_HHMMSS[:2]), int(start_time_HHMMSS[2:4]), int(start_time_HHMMSS[4:6]))
    while _datetime + timedelta(seconds=interval) < datetime.now():
        _datetime =  _datetime + timedelta(seconds=interval)
    # 
    _datetime = (_datetime + timedelta(seconds=interval))
    return _datetime

# ----------------------------------------------------------------------------------------------------------------------

strategyADXDMIHT_v1_2_iMainThread_exitFlag = False
def strategyADXDMIHT_v1_2_i_MainThread():
    """
    """
    global strategyADXDMIHT_v1_2_iMainThread_exitFlag
    hour, minute, seconds = list(map(int, wrap(parameter_dict['trade_start_time'], 2)))
    pause.until(datetime.today().replace(hour=hour, minute=minute, second=seconds))
    # 
    while not strategyADXDMIHT_v1_2_iMainThread_exitFlag:
        strategyADXDMIHT_v1_2_i_Main()
        pause_datetime = generateNextDateTimeWithInterval(start_time_HHMMSS=parameter_dict['trade_start_time'], interval=300)
        # logger.debug('Sleeping | Until: {}'.format(pause_datetime))
        pause.until(pause_datetime)
    logger.info('Exiting -> strategyADXDMIHT_v1_2_iMainThread')


checkStopLossThread_exitFlag = False
def checkStopLossThread(wait_interval=10):
    """
    """
    global checkStopLossThread_exitFlag
    pause.until(datetime.today().replace(hour=11, minute=00, second=10))
    # 
    while not checkStopLossThread_exitFlag:
        checkStopLoss()
        # logger.debug('Sleeping | wait_interval: {0}'.format(wait_interval))
        time.sleep(wait_interval)
    logger.info('Exiting -> checkStopLossThread')


activeThreadsMonitoringThread_exitFlag = False
def activeThreadsMonitoringThread(wait_interval=30):
    """
    """
    global activeThreadsMonitoringThread_exitFlag
    while not activeThreadsMonitoringThread_exitFlag:
        activeThreadsMonitoring()
        # logger.debug('Sleeping | wait_interval: {0}'.format(wait_interval))
        time.sleep(wait_interval)
    logger.info('Exiting -> activeThreadsMonitoringThread')


raiseNetworkErrorThread_exitFlag = False
def raiseNetworkErrorThread(wait_interval=30):
    """
    """
    global raiseNetworkErrorThread_exitFlag
    while not raiseNetworkErrorThread_exitFlag:
        raiseNetworkError(logger=logger)
        # logger.debug('Sleeping | wait_interval: {0}'.format(wait_interval))
        time.sleep(wait_interval)
    logger.info('Exiting -> raiseNetworkErrorThread')


def shutdownAllThreads():
    """
    """
    global strategyADXDMIHT_v1_2_iMainThread_exitFlag
    global checkStopLossThread_exitFlag
    global activeThreadsMonitoringThread_exitFlag
    global raiseNetworkErrorThread_exitFlag
    # 
    strategyADXDMIHT_v1_2_iMainThread_exitFlag = True
    checkStopLossThread_exitFlag = True
    activeThreadsMonitoringThread_exitFlag = True
    raiseNetworkErrorThread_exitFlag = True


def processShutdownMechanism():
    pause.until(datetime.today().replace(hour=15, minute=24, second=50))
    logger.info('Starting processShutdownMechanism->shutdownAllThreads')
    shutdownAllThreads()
    pause.until(datetime.today().replace(hour=15, minute=25, second=5))
    logger.info('Starting processShutdownMechanism->exitMarketOrderTrade')
    exitMarketOrderTrade()
    playAudioFromWavFile_v1(os.path.join(MODULE_SOUND_DIR, 'Data', 'Notification', 'Notification03.wav'))
    populateOrderManagementDFStatus(client=client, logger=logger)
    populateOrderManagementDFWithExecutionPrice(client=client, logger=logger)
    saveOrderManagementDFToDisk()


def saveOrderManagementDFToDisk():
    """
    **Need a way to not overwrite the existing file. Else all the order information will be lost
    """
    logger.debug('Saving-orderManagementDF-To-Disk ')
    file_name_csv = os.path.join(parameter_dict['directory_path'], 'OrderManagementDF_'+parameter_dict['strategy_name']+'.csv')
    file_name_pickle = os.path.join(parameter_dict['directory_path'], 'OrderManagementDF_'+parameter_dict['strategy_name']+'.pickle')
    LibOrderManagement.orderManagementDF.to_csv(file_name_csv)
    LibOrderManagement.orderManagementDF.to_pickle(file_name_pickle)
    writeTextToFile(file_path=os.path.join(file_name_csv.split('.')[0]+'_Tabulate'+'.sql'), text=tabulate(LibOrderManagement.orderManagementDF, headers='keys', tablefmt='psql'))

# ----------------------------------------------------------------------------------------------------------------------

initializeMainProcess()
# loadTradeStatusFromDisk()

strategyADXDMIHT_v1_2_i_MainThread_exitFlag = False
strategyADXDMIHT_v1_2_i_MainThread_thread = threading.Thread(target=strategyADXDMIHT_v1_2_i_MainThread, name='strategyADXDMIHT_v1_2_i_MainThread', daemon=True)
strategyADXDMIHT_v1_2_i_MainThread_thread.start()

# checkStopLossThread_exitFlag = False
# checkStopLossThread_thread = threading.Thread(target=checkStopLossThread, name='checkStopLossThread', daemon=True, kwargs={'wait_interval':10})
# checkStopLossThread_thread.start()

raiseNetworkErrorThread_exitFlag = False
raiseNetworkErrorThread_thread = threading.Thread(target=raiseNetworkErrorThread, name='raiseNetworkErrorThread', daemon=True, kwargs={'wait_interval':30})
raiseNetworkErrorThread_thread.start()

activeThreadsMonitoringThread_exitFlag = False
activeThreadsMonitoringThread_thread = threading.Thread(target=activeThreadsMonitoringThread, name='activeThreadsMonitoringThread', daemon=True, kwargs={'wait_interval':30})
activeThreadsMonitoringThread_thread.start()

processShutdownMechanism_thread = threading.Thread(target=processShutdownMechanism, name='processShutdownMechanism', daemon=True)
processShutdownMechanism_thread.start()

# ----------------------------------------------------------------------------------------------------------------------
# Development

populateOrderManagementDFStatus(client=client, logger=logger)
populateOrderManagementDFWithExecutionPrice(client=client, logger=logger)
printTabulateDataFrame(LibOrderManagement.orderManagementDF)

# ----------------------------------------------------------------------------------------------------------------------
