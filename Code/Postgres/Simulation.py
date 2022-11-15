"""
CREATE TABLE simulation (
    TradeDate          TEXT NOT NULL,
    SimulationDate     TEXT NOT NULL,
    StrategyName       TEXT NOT NULL,
    Instrument         TEXT NOT NULL,
    TradeTypeI         TEXT NOT NULL,
    TradeTimeI         TEXT NOT NULL,
    TradePriceI        FLOAT,
    TradeTypeF         TEXT NOT NULL,
    TradeTimeF         TEXT NOT NULL,
    TradePriceF        FLOAT,
    StopLoss           FLOAT,
    Target             FLOAT,
    Pnl                FLOAT,
    Comment            VARCHAR(10000)
    )
"""

DATABASE = 'shashank'
TABLE_NAME = 'simulation'


def makeInsertStringFromDictionary(table_name, dictionary):
    """
    makeInsertStringFromDictionary(table_name=TABLE_NAME, dictionary=input_dict)
    """
    coloumns = list(dictionary.keys())
    #
    position = "INSERT INTO " + table_name + "("
    for r in range(0,len(coloumns)):
        position = position + coloumns[r] + ","
        if r == len(coloumns) - 1:
            position = position[:-1] + ") "
    #
    element = 'VALUES ('
    for coloumn in coloumns:
        if isinstance(dictionary[coloumn], str):
            element = element + "'" + dictionary[coloumn] + "'" + ','
        elif isinstance(dictionary[coloumn], int):
            element = element + str(dictionary[coloumn]) + ','
    #
    element = (element[:-1]) + ')'
    full_string = position + ' ' + element
    return full_string


def insertPostgresDatabse(database, table_name, data_to_insert):
    import psycopg2
    #
    # variables
    hostname = 'localhost'
    username = 'postgres'
    Pwd = 0
    port_id = 5432
    #
    conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = Pwd,
                port = port_id)
    #
    cur = conn.cursor()
    #
    if isinstance(data_to_insert, dict):
        insert = makeInsertStringFromDictionary(table_name, data_to_insert)
        print(insert)
        cur.execute(insert)
        conn.commit()
    #
    elif isinstance(data_to_insert, list):
        for dictionary in data_to_insert:
            insert = makeInsertStringFromDictionary(table_name, dictionary)
            cur.execute(insert)
            conn.commit()


def inputElseDefault(input_text=None, default_value=None):
    input_string = input(input_text)
    if input_string == '':
        return default_value
    return input_string


def chooseStrategyName(default_value=None):
    """
    """
    strategy_name_list = ['STRATEGY-1', 'STRATEGY-2', 'STRATEGY-3']
    print("\n\nChoose A Strategy")
    for e, s in enumerate(strategy_name_list):
        print(e, s)
    # 
    _input = input()
    if _input == '':
        return default_value
    elif int(_input) > 0 and int(_input) < len(strategy_name_list):
        return strategy_name_list[int(_input)]
    else:
        return default_value




def userInput():
    from datetime import datetime
    print("\n\nChoose An Option")
    input_dict = {}
    input_dict['TradeDate']         = inputElseDefault(input_text='TradeDate : ' , default_value=None)
    input_dict['SimulationDate']    = inputElseDefault(input_text='SimulationDate : ' , default_value=datetime.now().strftime('%Y-%m-%d'))
    input_dict['StrategyName']      = chooseStrategyName(default_value='NO-STRATEGY')
    input_dict['Instrument']        = inputElseDefault(input_text='InstrumentName : ' , default_value=None)
    input_dict['TradeTypeI']        = inputElseDefault(input_text='TradeTypeI : ' , default_value=None)
    input_dict['TradeTimeI']        = inputElseDefault(input_text='TradeTimeI : ' , default_value=None)
    input_dict['TradePriceI']       = int(inputElseDefault(input_text='TradePriceI ', default_value=-1))
    input_dict['TradeTypeF']        = inputElseDefault(input_text='TradeTypeF' , default_value=None)
    input_dict['TradeTimeF']        = inputElseDefault(input_text='TradeTimeF' , default_value=None)
    input_dict['TradePriceF']       = int(inputElseDefault(input_text='TradePriceF : ' , default_value=-1))
    input_dict['StopLoss']          = int(inputElseDefault(input_text='StopLoss: ' , default_value=-1))
    input_dict['Target']            = int(inputElseDefault(input_text='Target: ' , default_value=-1))
    input_dict['Comment']           = inputElseDefault(input_text='Comment : ' , default_value='')
    # 
    return input_dict


def simulation(database=DATABASE, table_name=TABLE_NAME):
    data_dict = userInput()
    data_dict['PnL'] = data_dict['TradePriceF'] - data_dict['TradePriceI']
    insertPostgresDatabse(database=database, table_name=table_name, data_to_insert=data_dict)