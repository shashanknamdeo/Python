
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
import threading
import pandas as pd
from textwrap import wrap
from pprint import pprint
from functools import reduce
from datetime import datetime
from datetime import timedelta
from tabulate import tabulate

import SysPath
from Logging import initializeLogger

from LibNSEUtils import getExpiryDateOfATradeDate

from LibWriteToFile import writeTextToFile

from LibLogin import TradeLogin

import LibOrderManagement
from LibOrderManagement import createOrderDict
from LibOrderManagement import processOrder
from LibOrderManagement import populateOrderManagementDFStatus
from LibOrderManagement import getExecutionPriceFromOrderReport
from LibOrderManagement import populateOrderManagementDFWithExecutionPrice

from LibInstruments import getInstrumentFNOTokens
from LibInstruments import getInstrumentIndexToken
from LibInstruments import fetchAndSaveInstrumentFNOTokens

from LibPlayAudioFromFile import playAudioFromWavFile_v1

from LoadIndexHistoricalData import convertIndexDataFrameTimeInterval
from LoadIndexHistoricalData import convertStringIntervalToIntMinutes

from FetchHistoricalData import fetchHistoricalDataParameterized

from LiveTradeUtilities import raiseNetworkError
from LiveTradeUtilities import fetchInstrumentLTPFromInstrumentToken

# ----------------------------------------------------------------------------------------------------------------------

global logger
global client
global instrumentDF
global parameter_dict

global active_trade_dict_CE
global active_trade_dict_PE

global initiate_trade
initiate_trade = False

# ----------------------------------------------------------------------------------------------------------------------

def initiateOptionMarketOrderTrade(option_type, strike_price, transaction_type, quantity):
    """
    """
    global parameter_dict
    # 
    trade_date        = parameter_dict['trade_date']
    instrument_name   = parameter_dict['instrument_name']
    expiry_week_ahead = parameter_dict['expiry_week_ahead']
    # 
    expiry_date       = getExpiryDateOfATradeDate(instrument_name=instrument_name, date=trade_date, week_ahead=expiry_week_ahead)
    option_token      = getInstrumentFNOTokens(instrument_name=instrument_name, expiry_date=expiry_date, strike_price=strike_price, option_type=option_type)
    option_ltp        = fetchInstrumentLTPFromInstrumentToken(client=client, logger=logger, instrument_token=option_token)
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
        'ltp_provisional' : option_ltp,
    }
    logger.info(order_dict)
    order_id = processOrder(client=client, order_dict=order_dict, logger=logger)
    # 
    if order_id:
        order_dict['transaction_order_id'] = order_id
        order_dict['transaction_status'] = 'OPEN'
        return order_dict
    elif order_id is None:
        playAudioFromWavFile_v1(os.path.join(MODULE_SOUND_DIR, 'Data', 'Emergency', 'Emergency01.wav'))
        raise('Order-Execution-Failed')
    return {}


def createActiveTradeDict(order_dict, margin_bandwidth, strike_price, quantity):
    """
    """
    global instrument_ltp_T1
    # 
    active_trade_dict = {}
    active_trade_dict['instrument_ltp_T1'] = instrument_ltp_T1
    active_trade_dict['margin_bandwidth']  = margin_bandwidth
    active_trade_dict['strike_price']      = strike_price
    active_trade_dict['quantity']          = quantity
    active_trade_dict['order_dict']        = order_dict
    return active_trade_dict


def strategy_v2_1_NB1():
    """
    """
    global initiate_trade
    global instrumentDF
    global parameter_dict
    global active_trade_dict_CE
    global active_trade_dict_PE
    global instrument_ltp_T1
    # 
    instrument_name          = parameter_dict['instrument_name']
    expiry_week_ahead        = parameter_dict['expiry_week_ahead']
    sell_trade_time          = parameter_dict['sell_trade_time']
    step_size                = parameter_dict['step_size']
    upper_strike_bandwidth   = parameter_dict['upper_strike_bandwidth']
    lower_strike_bandwidth   = parameter_dict['lower_strike_bandwidth']
    interval                 = parameter_dict['interval']
    upper_strike_step_size   = parameter_dict['upper_strike_step_size']
    lower_strike_step_size   = parameter_dict['lower_strike_step_size']
    # 
    row = instrumentDF.iloc[-1]
    logger.debug('| trade_datetime: {} | open: {:7.2f} | high: {:7.2f} | low: {:7.2f} | close: {:7.2f} |' \
        .format(row.trade_datetime, row.open, row.high, row.low, row.close))
    # 
    # Sell-Iron-Condor-Trade-Initialization
    if not initiate_trade:
        instrument_ltp_T1         = row.close
        roundoff_instrument_price = round(int(instrument_ltp_T1)/step_size)*step_size
        upper_strike_price        = roundoff_instrument_price + upper_strike_bandwidth
        lower_strike_price        = roundoff_instrument_price - lower_strike_bandwidth
        # 
        lot_quantity         = parameter_dict['lot_quantity']
        quantity             = int(lot_quantity*INSTRUMENT_LOT_SIZE_DICT[instrument_name])
        #
        order_dict_CE        = initiateOptionMarketOrderTrade(strike_price=upper_strike_price, option_type='CE', transaction_type='SELL', quantity=quantity)
        active_trade_dict_CE = createActiveTradeDict(order_dict=order_dict_CE, margin_bandwidth=parameter_dict['upper_margin_bandwidth'], strike_price=upper_strike_price, quantity=quantity)
        # 
        order_dict_PE        = initiateOptionMarketOrderTrade(strike_price=lower_strike_price, option_type='PE', transaction_type='SELL', quantity=quantity)
        active_trade_dict_PE = createActiveTradeDict(order_dict=order_dict_PE, margin_bandwidth=parameter_dict['lower_margin_bandwidth'], strike_price=lower_strike_price, quantity=quantity)
        # 
        initiate_trade = True
        saveTradeStatusToDisk()
        logger.debug('active_trade_dict_CE: {}'.format(active_trade_dict_CE))
        logger.debug('active_trade_dict_PE: {}'.format(active_trade_dict_PE))
        playAudioFromWavFile_v1(os.path.join(MODULE_SOUND_DIR, 'Data', 'Notification', 'Notification03.wav'))
    # 
    # 
    buy_trade_time_CE = buy_trade_time_PE = buy_trade_time = row['trade_time']
    instrument_ltp_T2_CE = instrument_ltp_T2_PE = instrument_ltp = instrumentDF[(instrumentDF.trade_time==buy_trade_time)].close.values[0]
    # 
    # Check-Upper-Initial-Range-Break -> CE_SHIFT_UPPER
    upper_margin_bandwidth = active_trade_dict_CE['margin_bandwidth']
    if (instrument_ltp - instrument_ltp_T1 >= upper_margin_bandwidth) and (instrument_ltp - instrument_ltp_T1 <= parameter_dict['upper_margin_threshold']):
        logger.debug('UPPER_MARGIN_BREACH -> SHIFTING_UPPER')
        upper_strike_price     = active_trade_dict_CE['strike_price']
        quantity_CE            = active_trade_dict_CE['quantity']
        order_dict_CE          = initiateOptionMarketOrderTrade(strike_price=upper_strike_price, option_type='CE', transaction_type='BUY', quantity=quantity_CE)
        upper_strike_price     = upper_strike_price + upper_strike_step_size
        upper_margin_bandwidth = upper_margin_bandwidth + upper_strike_step_size
        order_dict_CE          = initiateOptionMarketOrderTrade(strike_price=upper_strike_price, option_type='CE', transaction_type='SELL', quantity=quantity_CE)
        active_trade_dict_CE   = createActiveTradeDict(order_dict=order_dict_CE, margin_bandwidth=upper_margin_bandwidth, strike_price=upper_strike_price, quantity=quantity_CE)
        saveTradeStatusToDisk()
        logger.debug('active_trade_dict_CE: {}'.format(active_trade_dict_CE))
        playAudioFromWavFile_v1(os.path.join(MODULE_SOUND_DIR, 'Data', 'Notification', 'Notification03.wav'))
    # 
    # Check-Lower-Initial-Range-Break -> PE_SHIFT_LOWER
    lower_margin_bandwidth = active_trade_dict_PE['margin_bandwidth']
    if (instrument_ltp_T1 - instrument_ltp >= lower_margin_bandwidth) and (instrument_ltp_T1 - instrument_ltp <= parameter_dict['lower_margin_threshold']):
        logger.debug('LOWER_MARGIN_BREACH -> SHIFTING_LOWER')
        lower_strike_price     = active_trade_dict_PE['strike_price']
        quantity_PE            = active_trade_dict_PE['quantity']
        order_dict_PE          = initiateOptionMarketOrderTrade(strike_price=lower_strike_price, option_type='PE', transaction_type='BUY', quantity=quantity_PE)
        lower_strike_price     = lower_strike_price - lower_strike_step_size
        lower_margin_bandwidth = lower_margin_bandwidth + lower_strike_step_size
        order_dict_PE          = initiateOptionMarketOrderTrade(strike_price=lower_strike_price, option_type='PE', transaction_type='SELL', quantity=quantity_PE)
        active_trade_dict_PE   = createActiveTradeDict(order_dict=order_dict_PE, margin_bandwidth=lower_margin_bandwidth, strike_price=lower_strike_price, quantity=quantity_PE)
        saveTradeStatusToDisk()
        logger.debug('active_trade_dict_PE: {}'.format(active_trade_dict_PE))
        playAudioFromWavFile_v1(os.path.join(MODULE_SOUND_DIR, 'Data', 'Notification', 'Notification03.wav'))


def exitMarketOrderTrade():
    """
    """
    upper_strike_price = active_trade_dict_CE['strike_price']
    lower_strike_price = active_trade_dict_PE['strike_price']
    quantity_CE = active_trade_dict_CE['quantity']
    quantity_PE = active_trade_dict_PE['quantity']
    # 
    order_dict_CE = initiateOptionMarketOrderTrade(strike_price=upper_strike_price, option_type='CE', transaction_type='BUY', quantity=quantity_CE)
    order_dict_PE = initiateOptionMarketOrderTrade(strike_price=lower_strike_price, option_type='PE', transaction_type='BUY', quantity=quantity_PE)


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


def strategy_v2_1_NB1_Main():
    """
    """
    global instrumentDF
    trade_date = parameter_dict['trade_date']
    try:
        instrumentDF = fetchHistoricalDataParameterized(instrument_name=parameter_dict['instrument_name'], start_date=trade_date, end_date=trade_date, interval=parameter_dict['interval'])
        validateInstrumentData()
        strategy_v2_1_NB1()
    except Exception as e:
        logger.exception(e, exc_info=True, stack_info=False)
        raise e


# ----------------------------------------------------------------------------------------------------------------------
# Management-Methods

def saveTradeStatusToDisk():
    """
    """
    global initiate_trade
    global instrument_ltp_T1
    global active_trade_dict_CE
    global active_trade_dict_PE
    # 
    json_object = {
        'initiate_trade'      : initiate_trade,
        'instrument_ltp_T1'   : instrument_ltp_T1,
        'active_trade_dict_CE': active_trade_dict_CE,
        'active_trade_dict_PE': active_trade_dict_PE
    }
    logger.debug('json_object: {}'.format(json_object))
    # 
    directory_path = parameter_dict['directory_path']
    with open(os.path.join(directory_path, 'strategy_v2_1_NB1_TradeState.json'), 'w+') as output_file:
        json.dump(json_object, output_file, indent=4, sort_keys=True)


def loadTradeStatusFromDisk():
    """
    """
    global initiate_trade
    global instrument_ltp_T1
    global active_trade_dict_CE
    global active_trade_dict_PE
    # 
    logger.debug('Loading-Trade-State-Fron-Disk')
    # 
    directory_path = parameter_dict['directory_path']
    with open(os.path.join(directory_path, 'strategy_v2_1_NB1_TradeState.json'), 'r') as input_file:
        json_object = json.load(input_file)
    # 
    initiate_trade       = json_object['initiate_trade']
    instrument_ltp_T1    = json_object['instrument_ltp_T1']
    active_trade_dict_CE = json_object['active_trade_dict_CE']
    active_trade_dict_PE = json_object['active_trade_dict_PE']
    # 
    logger.debug('initiate_trade: {} | instrument_ltp_T1: {}'.format(initiate_trade, instrument_ltp_T1))
    logger.debug('active_trade_dict_CE: {}'.format(active_trade_dict_CE))
    logger.debug('active_trade_dict_PE: {}'.format(active_trade_dict_PE))



def activeThreadsMonitoring():
    """
    """
    file_path = os.path.join(GOOGLEDRIVE_TRADE_LOGS_DIR, 'LIVE', 'ActiveThreadMonitoring', 'ActiveThreadsName_strategy_v2_1_NB1.txt')
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

def initializeMainProcess():
    """
    """
    global logger
    global client
    global parameter_dict 
    # 
    directory_path = os.path.join(GOOGLEDRIVE_TRADE_LOGS_DIR, 'LIVE','LIVE_'+datetime.now().strftime('%Y%m%d'))
    file_name = 'strategy_v2_1_NB1'+'_'+datetime.now().strftime('%Y%m%d_%H%M%S')+'.log'
    logger = initializeLogger(directory_path=directory_path, file_name=file_name)
    # 
    parameter_dict = {
        'strategy_name'          : 'strategy_v2_1_NB1',
        'instrument_name'        : 'NIFTYBANK',
        'step_size'              : 100,
        'sell_trade_time'        : '0915',
        'buy_trade_time'         : '1524',
        'expiry_week_ahead'      : 0,
        'lower_strike_bandwidth' : 400,
        'upper_strike_bandwidth' : 400,
        'lower_margin_bandwidth' : 200,
        'upper_margin_bandwidth' : 200,
        'lower_margin_threshold' : 1000,
        'upper_margin_threshold' : 1000,
        'lower_strike_step_size' : 100,
        'upper_strike_step_size' : 100,
        'trailing_stoploss'      : None,
        'stoploss_percent'       : None,
        'target_price'           : None,
        'lot_quantity'           : 2,
        'interval'               : '3MINUTE', # Represent the interval of the algo iteration.
        # 
        'directory_path'         : directory_path,
        'trade_date'             : datetime.now().strftime('%Y%m%d'),
        'trade_start_time'       : '091810',
        'trade_end_time'         : '152700',
    }
    logger.info('parameter_dict: {}'.format((json.dumps(parameter_dict, indent=4))))
    # 
    try:
        client = TradeLogin()
        logger.debug('Connection-Established')
    except urllib3.exceptions.MaxRetryError as e:
        logger.error(e)
        logger.debug('Check-Network-Connection')
        sys.exit(1)
    # 
    # fetchAndSaveInstrumentFNOTokens() # Implement to download only once a dat at-maximum.
    return True

# ----------------------------------------------------------------------------------------------------------------------

strategy_v2_1_NB1_MainThread_exitFlag = False
def strategy_v2_1_NB1_MainThread():
    """
    """
    global strategy_v2_1_NB1_MainThread_exitFlag
    hour, minute, seconds = list(map(int, wrap(parameter_dict['trade_start_time'], 2)))
    pause.until(datetime.today().replace(hour=hour, minute=minute, second=seconds))
    # 
    while not strategy_v2_1_NB1_MainThread_exitFlag:
        strategy_v2_1_NB1_Main()
        pause_datetime = generateNextDateTimeWithInterval(start_time_HHMMSS=parameter_dict['trade_start_time'], interval=180)
        # logger.debug('Sleeping | Until: {}'.format(pause_datetime))
        pause.until(pause_datetime)
    logger.info('Exiting -> strategy_v2_1_NB1_MainThread')


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
    global strategy_v2_1_NB1_MainThread_exitFlag
    global checkStopLossThread_exitFlag
    global activeThreadsMonitoringThread_exitFlag
    global raiseNetworkErrorThread_exitFlag
    # 
    strategy_v2_1_NB1_MainThread_exitFlag = True
    checkStopLossThread_exitFlag = True
    activeThreadsMonitoringThread_exitFlag = True
    raiseNetworkErrorThread_exitFlag = True


def processShutdownMechanism():
    pause.until(datetime.today().replace(hour=15, minute=27, second=55))
    logger.info('Starting processShutdownMechanism->shutdownAllThreads')
    shutdownAllThreads()
    pause.until(datetime.today().replace(hour=15, minute=28, second=0))
    logger.info('Starting processShutdownMechanism->exitMarketOrderTrade')
    exitMarketOrderTrade()
    playAudioFromWavFile_v1(os.path.join(MODULE_SOUND_DIR, 'Data', 'Notification', 'Notification03.wav'))
    populateOrderManagementDFStatus(client=client, logger=logger)
    populateOrderManagementDFWithExecutionPrice(client=client, logger=logger)
    saveOrderManagementDFToDisk()

# ----------------------------------------------------------------------------------------------------------------------

initializeMainProcess()
# loadTradeStatusFromDisk()

strategy_v2_1_NB1_MainThread_exitFlag = False
strategy_v2_1_NB1_MainThread_thread = threading.Thread(target=strategy_v2_1_NB1_MainThread, name='strategy_v2_1_NB1_MainThread', daemon=True)
strategy_v2_1_NB1_MainThread_thread.start()

raiseNetworkErrorThread_exitFlag = False
raiseNetworkErrorThread_thread = threading.Thread(target=raiseNetworkErrorThread, name='raiseNetworkErrorThread', daemon=True, kwargs={'wait_interval':30})
raiseNetworkErrorThread_thread.start()

activeThreadsMonitoringThread_exitFlag = False
activeThreadsMonitoringThread_thread = threading.Thread(target=activeThreadsMonitoringThread, name='activeThreadsMonitoringThread', daemon=True, kwargs={'wait_interval':30})
activeThreadsMonitoringThread_thread.start()

processShutdownMechanism_thread = threading.Thread(target=processShutdownMechanism, name='processShutdownMechanism', daemon=True)
processShutdownMechanism_thread.start()

# ----------------------------------------------------------------------------------------------------------------------


def moveOptionStrikeUpDownBandwidth(active_trade_dict, strike_price_move_bandwidth):
    """
    Moving strike_price up/down without modifying margin_bandwidth. So the algorithm still would work on existing 
    margin_bandwidth rule.
    
    active_trade_dict_CE = moveOptionStrikeUpDown(active_trade_dict=active_trade_dict_PE, strike_price_move_bandwidth=+100)
    active_trade_dict_CE = moveOptionStrikeUpDown(active_trade_dict=active_trade_dict_PE, strike_price_move_bandwidth=-100)
    """
    strike_price = active_trade_dict['strike_price']
    quantity     = active_trade_dict['quantity']
    option_type  = active_trade_dict['order_dict']['option_type']
    order_dict = initiateOptionMarketOrderTrade(strike_price=strike_price, option_type=option_type, transaction_type='BUY', quantity=quantity)
    # 
    strike_price_modified = strike_price+strike_price_move_bandwidth
    order_dict_modified = initiateOptionMarketOrderTrade(strike_price=strike_price_modified, option_type=option_type, transaction_type='SELL', quantity=quantity)
    # 
    active_trade_dict['strike_price'] = strike_price_modified
    active_trade_dict['order_dict']   = order_dict_modified
    # 
    return active_trade_dict


def changeOptionLotAddSubQuantity(active_trade_dict, quantity_change):
    """
    **Executing this function will produce a new order_dict. How to handle this?
    """
    strike_price = active_trade_dict['strike_price']
    option_type  = active_trade_dict['order_dict']['option_type']
    # 
    transaction_type = 'SELL' if quantity_change > 0 else 'BUY'
    order_dict   = initiateOptionMarketOrderTrade(strike_price=strike_price, option_type=option_type, transaction_type=transaction_type, quantity=abs(quantity_change))
    active_trade_dict['quantity'] = active_trade_dict['quantity']+quantity_change
    return active_trade_dict


def moveOptionStrikeUpDown():
    """
    Improvements:
    1. Needs validation for Instrument step size multiple.
    """
    global active_trade_dict_CE
    global active_trade_dict_PE
    # 
    try:
        print("\n\nChoose Move-Option and Move-Stepsize")
        option_type = input('OPTION_TYPE[CE|PE] : ').strip()
        strike_price_move_bandwidth = int(input('MOVE_STEPSIZE[x100]: ').strip())
        # 
        if option_type.upper() == 'CE':
            active_trade_dict_CE = moveOptionStrikeUpDownBandwidth(active_trade_dict=active_trade_dict_CE, strike_price_move_bandwidth=strike_price_move_bandwidth)
            logger.debug(active_trade_dict_CE)
            saveTradeStatusToDisk()
        elif option_type.upper() == 'PE':
            active_trade_dict_PE = moveOptionStrikeUpDownBandwidth(active_trade_dict=active_trade_dict_PE, strike_price_move_bandwidth=strike_price_move_bandwidth)
            logger.debug(active_trade_dict_PE)
            saveTradeStatusToDisk()
        else:
            logger.debug('Invalid-Move-Option')
    except Exception as e:
        logger.exception(e)


def changeOptionLotAddSub():
    """
    """
    global active_trade_dict_CE
    global active_trade_dict_PE
    # 
    try:
        instrument_name = parameter_dict['instrument_name']
        lot_quantity = 1
        quantity = int(lot_quantity*INSTRUMENT_LOT_SIZE_DICT[instrument_name])
        # 
        print('\n\nChoose Lot-Change-Options')
        print('AB. ADD-[1]Lot-On-Both-Option')
        print('SB. SUB-[1]Lot-On-Both-Option')
        print('AC. ADD-[1]Lot-On-CE-Option')
        print('SC. SUB-[1]Lot-On-CE-Option')
        print('AP. ADD-[1]Lot-On-PE-Option')
        print('SP. SUB-[1]Lot-On-PE-Option')
        # 
        option = input(': ').strip()
        if option.lower() == 'ab':
            active_trade_dict_CE = changeOptionLotAddSubQuantity(active_trade_dict=active_trade_dict_CE, quantity_change=quantity)
            active_trade_dict_PE = changeOptionLotAddSubQuantity(active_trade_dict=active_trade_dict_PE, quantity_change=quantity)
        elif option.lower() == 'sb':
            active_trade_dict_CE = changeOptionLotAddSubQuantity(active_trade_dict=active_trade_dict_CE, quantity_change=-quantity)
            active_trade_dict_PE = changeOptionLotAddSubQuantity(active_trade_dict=active_trade_dict_PE, quantity_change=-quantity)
        elif option.lower() == 'ac':
            active_trade_dict_CE =changeOptionLotAddSubQuantity(active_trade_dict=active_trade_dict_CE, quantity_change=quantity)
        elif option.lower() == 'sc':
            active_trade_dict_CE =changeOptionLotAddSubQuantity(active_trade_dict=active_trade_dict_CE, quantity_change=-quantity)
        elif option.lower() == 'ap':
            active_trade_dict_PE =changeOptionLotAddSubQuantity(active_trade_dict=active_trade_dict_PE, quantity_change=quantity)
        elif option.lower() == 'sp':
            active_trade_dict_PE = changeOptionLotAddSubQuantity(active_trade_dict=active_trade_dict_PE, quantity_change=-quantity)
        else:
            logger.debug('Skipping-Due-To-Invalid-Option')
        saveTradeStatusToDisk()
    except Exception as e:
        logger.exception(e)


def strategyTradeManagementMain():
    """
    """
    def userInput():
        print("\n\nChoose An Option")
        print('M. Execute -> moveOptionStrikeUpDown')
        print('C. Execute -> changeOptionLotAddSub')
        print('X. Settings')
        print('Q. Quit')
        option = input(': ').strip()
        return option
    # 
    option = userInput()
    if option.lower() == 'm':
        moveOptionStrikeUpDownMain()
    elif option.lower() == 'l':
        changeOptionLotIncreaseDecreaseMain()
    elif option.lower() == 'q':
        return None


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
# DEVELOPMENT

printTabulateDataFrame(LibOrderManagement.orderManagementDF)
populateOrderManagementDFWithExecutionPrice(client=client, logger=logger)

# ----------------------------------------------------------------------------------------------------------------------
