def toDescribeDataWithHighLow(data_path):
    instrumentDF = pd.read_csv(data_path)
    #
    instrumentDF['high-low_percent'] = (abs(instrumentDF['High']-instrumentDF['Low'])/instrumentDF['Low'])*100
    return instrumentDF['high-low_percent'].describe()
    