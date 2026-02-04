import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import pandas as pd
from pprint import pprint

from GlobalFunctions import printTabulateDataFrame

global positionDF

def fetchMargin():
    """
    """
    client_nmargin = client.margin()
    margin_total = int(client_nmargin['Success']['equity'][0]['cash']['totalMargin'])
    margin_available = int(client_nmargin['Success']['equity'][0]['cash']['marginAvailable'])
    margin_utilized = int(client_nmargin['Success']['equity'][0]['cash']['marginUtilised'])
    # 
    print('| margin_total: {:,} | margin_available: {:,} | margin_utilized: {:,} |'.format(margin_total, margin_available, margin_utilized))


def FetchOpenPositions(position_type='TODAYS'):
    """
    position_type=[TODAYS/OPEN]
    """
    global positionDF
    position_open = client.positions(position_type=position_type)['Success']
    positionDF = pd.DataFrame(position_open)
    positionDF = positionDF[positionDF.optionType!='']
    positionDF = positionDF.sort_values(by=['symbol', 'optionType', 'strikePrice'], ascending=[False, True, False])
    positionDF = positionDF[positionDF.netTrdQtyLot!=0]
    positionDF['premium'] = (positionDF.netTrdQtyLot*positionDF.lastPrice)/positionDF.marketLot
    positionDF = positionDF[['symbol', 'strikePrice', 'optionType', 'netTrdQtyLot', 'premium', 'lastPrice', 'realizedPL', 'instrumentToken', 'expiryDate', 'segment']]
    printTabulateDataFrame(positionDF)
    return positionDF


def openPremiumDetails(position_type='TODAYS'):
    """
    """
    positionDF = FetchOpenPositions(position_type=position_type)
    positionDF = positionDF[positionDF.segment=='OI']
    NIFTY_CE_DF = positionDF[(positionDF.symbol=='NIFTY') & (positionDF.optionType=='CE')]
    NIFTY_PE_DF = positionDF[(positionDF.symbol=='NIFTY') & (positionDF.optionType=='PE')]
    NIFTY_CE_premium = sum(NIFTY_CE_DF.netTrdQtyLot*NIFTY_CE_DF.lastPrice/50)
    NIFTY_PE_premium = sum(NIFTY_PE_DF.netTrdQtyLot*NIFTY_PE_DF.lastPrice/50)
    # 
    NIFTYBANK_CE_DF = positionDF[(positionDF.symbol=='BANKNIFTY') & (positionDF.optionType=='CE')]
    NIFTYBANK_PE_DF = positionDF[(positionDF.symbol=='BANKNIFTY') & (positionDF.optionType=='PE')]
    NIFTYBANK_CE_premium = sum(NIFTYBANK_CE_DF.netTrdQtyLot*NIFTYBANK_CE_DF.lastPrice/15)
    NIFTYBANK_PE_premium = sum(NIFTYBANK_PE_DF.netTrdQtyLot*NIFTYBANK_PE_DF.lastPrice/15)
    # 
    NIFTY_CE_NET_QUANTITY = sum(NIFTY_CE_DF.netTrdQtyLot)
    NIFTY_PE_NET_QUANTITY = sum(NIFTY_PE_DF.netTrdQtyLot)
    NIFTYBANK_CE_NET_QUANTITY = sum(NIFTYBANK_CE_DF.netTrdQtyLot)
    NIFTYBANK_PE_NET_QUANTITY = sum(NIFTYBANK_PE_DF.netTrdQtyLot)
    # 
    NIFTY_NET_PREMIUM     = positionDF[(positionDF.symbol=='NIFTY')].apply(lambda x: x.netTrdQtyLot*x.lastPrice, axis=1).sum()
    NIFTYBANK_NET_PREMIUM = positionDF[(positionDF.symbol=='BANKNIFTY')].apply(lambda x: x.netTrdQtyLot*x.lastPrice, axis=1).sum()
    NET_PREMIUM_CE        = positionDF[(positionDF.optionType=='CE')].apply(lambda x: x.netTrdQtyLot*x.lastPrice, axis=1).sum()
    NET_PREMIUM_PE        = positionDF[(positionDF.optionType=='PE')].apply(lambda x: x.netTrdQtyLot*x.lastPrice, axis=1).sum()
    # 
    print('| NIFTY       | CE_PREMIUM:     {:<8.2f} | PE_PREMIUM:     {:<8.2f} |'.format(NIFTY_CE_premium, NIFTY_PE_premium))
    print('|             | CE_QUANTITY:    {:<8.2f} | PE_QUANTITY:    {:<8.2f} |'.format(NIFTY_CE_NET_QUANTITY, NIFTY_PE_NET_QUANTITY))
    print('| NIFTYBANK   | CE_PREMIUM:     {:<8.2f} | PE_PREMIUM:     {:<8.2f} |'.format(NIFTYBANK_CE_premium, NIFTYBANK_PE_premium))
    print('|             | CE_QUANTITY:    {:<8.2f} | PE_QUANTITY:    {:<8.2f} |'.format(NIFTYBANK_CE_NET_QUANTITY, NIFTYBANK_PE_NET_QUANTITY))
    print('| PREMIUM_NET | NIFTY:          {:<8.1f} | NIFTYBANK:      {:<8.1f} |'.format(NIFTY_NET_PREMIUM, NIFTYBANK_NET_PREMIUM))
    print('| PREMIUM_NET | NET_PREMIUM_CE: {:<8.1f} | NET_PREMIUM_PE: {:<8.1f} |'.format(NET_PREMIUM_CE, NET_PREMIUM_PE))


def ExitAllOpenPositions():
    """
    client.place_order(instrument_token=24392, order_type='N', transaction_type='SELL', quantity=50, price=0)
    """
    def createExitOrderDict(row):
        if row.netTrdQtyLot > 0:
            transaction_type = 'SELL'
        elif row.netTrdQtyLot < 0:
            transaction_type = 'BUY'
        # 
        return {
            'instrument_token' : int(row.instrumentToken),
            'order_type'       : 'N',
            'transaction_type' : transaction_type,
            'quantity'         : abs(int(row.netTrdQtyLot)),
            'price'            : 0
        }
    # 
    option = input('Exit-All-Open-Positions-Confirmation: ').strip()
    option_reconfirm = input('Exit-All-Open-Positions-Confirmation: ').strip()
    if option.lower() == 'yes' and option_reconfirm.lower() == 'yes':
        positionDF = FetchOpenPositions()
        for _, row in positionDF.iterrows():
            # row = row.squeeze()
            _order_dict = createExitOrderDict(row=row)
            response = client.place_order(**_order_dict)
            order_id = response['Success']['NSE']['orderId']
            print('order_id: {} | _order_dict: {}'.format(order_id, _order_dict))
    else:
        print('Confirmation-Denied: Skipping-Exit-All-Open-Positions')


def LiveTradeManagementMain():
    """
    """
    def userInput():
        print("\n\nChoose An Option")
        print('M.  Execute -> fetchMargin')
        print('P.  Execute -> FetchOpenPositions')
        print('O.  Execute -> openPremiumDetails')
        print('O2. Execute -> openPremiumDetails -> OPEN')
        print('E:  Execute -> ExitAllOpenPositions')
        print('X.  Settings')
        print('Q.  Quit')
        option = input(': ').strip()
        return option
    # 
    while True:
        option = userInput()
        print('\n'*40)
        if option.lower() == 'm':
            fetchMargin()
        elif option.lower() == 'p':
            FetchOpenPositions()
        elif option.lower() == 'o':
            openPremiumDetails()
        elif option.lower() == 'o2':
            openPremiumDetails(position_type='OPEN')
        elif option.lower() == 'e':
            ExitAllOpenPositions()
        elif option.lower() == 'x':
            pass
            # changeSettings()
        elif option.lower() == 'q':
            exit()
        print('+'+'-'*140+'+', '\n')


if __name__ == '__main__':
    print("Module: LiveTredeManagement [Direct Invocation]")
    LiveTradeManagementMain()
else:
    print("Module: LiveTredeManagement [Imported]")


# --------------------------------------------------------------------------------------------------
# DEVELOPMENT

from LibOrderManagement import getExecutionPriceFromOrderReport

def function():
    response = client.place_order(instrument_token=63905, quantity=50, transaction_type='SELL', order_type='N', price=0)
    order_id = response['Success']['NSE']['orderId']
    execution_price = getExecutionPriceFromOrderReport(client=client, logger=None, order_id=order_id)
    print(execution_price)



# orderDF[orderDF.status=='OPN'] -> OPEN ORDER