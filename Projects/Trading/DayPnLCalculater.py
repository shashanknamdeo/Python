import pandas as pd

def getHoldingDataFromConsole():
    print("Paste Holding csv-data:")
    contents = []
    while True:
        line = input()
        if line.strip() == '':
            break
        contents.append(line)
    pnl_dict = {} 
    instrument_quantity_dict_holding = {}
    for line in contents:
        date, _, pnl = line.split('  ')
        pnl_dict[date] = int(pnl)
    print(pnl_dict)
    return pd.DataFrame(pnl_dict, index=[0]).T


_df = getHoldingDataFromConsole()
_df['']_df[_df[0]>0]