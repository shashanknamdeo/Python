


parameter_dict = {
    'instrument_name'        :'NIFTY',
    'start_date'             : '20230101',
    'end_date'               : '20230731',
    'expiry_week_ahead'      : 0,
    'strike_price_bandwidth' : 0,
    'timeframe_dict'         : {'MAIN' : '5MINUTE', 'HALFTREND' : '5MINUTE', 'DMI' : '15MINUTE', 'ADX' : '5MINUTE'},
    'condition_dict'         : {'ADX' : 25}
}

-> (920.65, 203)


Development

instrument_name = 'NIFTY'
timeframe_dict = {'MAIN' : 'MINUTE', 'HALFTREND' : 'MINUTE', 'DMI' : '3MINUTE', 'ADX' : 'MINUTE'}
start_date = '20230801'
end_date = '20230808'
condition_dict = {'ADX' : 20}

DF = createMainDF(instrument_name=instrument_name, timeframe_dict=timeframe_dict, start_date=start_date, end_date=end_date, verbose=1)

    current_date         = bt_start_date = parameter_dict['bt_start_date']
    bt_end_date          = parameter_dict['bt_end_date']
    expiry_week_ahead    = parameter_dict['expiry_week_ahead']
    upper_near_bandwidth = parameter_dict['upper_near_bandwidth']
    lower_near_bandwidth = parameter_dict['lower_near_bandwidth']
    count = 0
    cummulative_pnl_points = 0
    # 
    logger.debug('parameter_dict: {}'.format(parameter_dict))
    # 
    indexDF = loadIndexHistoricalData(instrument_name='NIFTY', interval='MINUTE', start_date='20220101', end_date=datetime.now().strftime('%Y%m%d'))
    # 
    while current_date <= bt_end_date:

        pnl_points = (CE_N_SELL_D1 - CE_N_BUY_D2) + (PE_N_SELL_D1 - PE_N_BUY_D2)
        cummulative_pnl_points = cummulative_pnl_points + pnl_points
        count = count + 1






--------------------------------------------------------------------------------------------------


def strategyDMIHalftrendMain():
    """
    """
    main_df = createMainDF(instrument_name=instrument_name, timeframe_dict=timeframe_dict, start_date=start_date, end_date=end_date, verbose=0)
    # 
    day_df_list = createDayDfList(main=main_df)
    # 
    TradeStartTime = findTradeStartTime(main_df=main_df, verbose=verbose)
    # 
    for day_df in day_df_list:
        day_df.reset_index(inplace = True, drop = True)
        day_df = day_df[TradeStartTime:]
        for i in range(len(df.axes[0])):
            


file_name = r'G:\My Drive\TradeData\IndexData\ZerodhaData\NIFTY\3MINUTE\MONTHLY\202308.csv'

day_df = pd.read_csv(file_name)

# perameters
timeframe = MINUTE
timeframe_dict = {'HALFTREND' : 'MINUTE', 'DMI' : '3MINUTE', 'ADX' : 'MINUTE'}
start_date = '20230801'
end_date = '20230808'


def calculatePNL(close, close_pre, new_trend, verbose=0):
    print (close, close_pre, new_trend) if verbose > 0 else None
    if new_trend == 1:
        pnl = close_pre - close
        print(pnl) if verbose > 0 else None
        return pnl
    if new_trend == -1:
        pnl = close - close_pre
        print(pnl) if verbose > 0 else None
        return pnl



ATR calculation

    trend = 0
    nextTrend = 0
    # 
    up = 0.0
    down = 0.0
    atrHigh = 0.0
    atrLow = 0.0
    # 
    arr_high = hlc_df["high"].to_numpy()
    arr_low = hlc_df["low"].to_numpy()
    arr_close = hlc_df["close"].to_numpy()
    # 
    # minhighprice = np.insert(numpy.delete(arr_high, -1), 0, None)
    # maxlowprice  = np.insert(numpy.delete(arr_low, -1), 0, None)
    # 
    atr100_arr =  ATR(arr_high, arr_low,arr_close, 100)
    if (amplitude != 2) or (channelDeviation != 2):
        atr100_arr = atr100_arr*(channelDeviation/amplitude)
    # 
    # arr_highprice = getHighestHigh(amplitude=amplitude, arr_high=arr_high)  # arr_highesthigh
    # arr_lowprice   = getLowestLow(amplitude=amplitude, arr_low=arr_low)      # arr_lowestlow 
    # 

def getHighestHigh(amplitude, arr_high):
    """
    # getHighestHigh(amplitude=3, arr_high=arr_high[40:50])
    """
    highest_high = []
    for i in range(amplitude, len(arr_high)):
        prev_highs = arr_high[i-amplitude:i]
        high = 0
        for element in prev_highs:
            if element > high:
                high  = element
        # 
        highest_high.append(high)
    # 
    for r in range(amplitude):
        highest_high.insert(0, None)
    # 
    return highest_high

def getLowestLow(amplitude, arr_low):
    """
    # getLowestLow(amplitude=3, arr_low=arr_low[40:50])
    """
    lowest_low = []
    for i in range(amplitude, len(arr_low)):
        prev_lows = arr_low[i-amplitude:i]
        low = float('inf')
        for element in prev_lows:
            if element < low:
                low  = element
        # 
        lowest_low.append(low)
    # 
    for r in range(amplitude):
        lowest_low.insert(0, None)
    # 
    return lowest_low



    hlc_df['plus_di']   = pd.DataFrame(plus_di).rename(columns = {0:'plus_di'})
    hlc_df['minus_di']  = pd.DataFrame(minus_di).rename(columns = {0:'minus_di'})
    hlc_df['adx']       = pd.DataFrame(adx_smooth).rename(columns = {0:'adx'})

if nextTrend == -ve
    maxLowPrice = max(lowPrice, prev_LowPrice)
# 
    if highma < maxLowPrice and close < prev_low
        trend = -ve
        nextTrend = +ve
        minHighPrice = highPrice
else
    minHighPrice = min(highPrice, prev_HighPrice)
# 
    if lowma > minHighPrice and close > prev_high
        trend = +ve
        nextTrend = -ve1
        maxLowPrice = lowPrice


if trend == +ve
    if trend_prev == -ve
        # if previous trend is -ve and if previus trend is not None
        up = down_prev
        arrowUp = up - atr2
    else
        up = na(up_prev) ? maxLowPrice : max(maxLowPrice, up_prev)
    atrHigh = up + dev
    atrLow = up - dev
elif trend == -ve
    if (trend_prev != none) and (trend_prev != -ve )
        # if previous trend is +ve and if previus trend is not None
        down = na(up_prev) ? up : up_prev
        arrowDown = down + atr2
    else
        down = na(down_prev) ? minHighPrice : min(minHighPrice, down_prev)
    atrHigh = down + dev
    atrLow = down - dev


1 = -ve
0 = +ve

trend_prev


if trend == +ve
    if (trend_prev != none) and (trend_prev != +ve)
        # if previous trend is -ve and if previus trend is not None
        up = na(down_prev) ? down : down_prev
        arrowUp = up - atr2
    else
        up = na(up_prev) ? maxLowPrice : max(maxLowPrice, up_prev)
    atrHigh = up + dev
    atrLow = up - dev
elif trend == -ve
    if (trend_prev != none) and (trend_prev != -ve )
        # if previous trend is +ve and if previus trend is not None
        down = na(up_prev) ? up : up_prev
        arrowDown = down + atr2
    else
        down = na(down_prev) ? minHighPrice : min(minHighPrice, down_prev)
    atrHigh = down + dev
    atrLow = down - dev


plot(atr(14))

//the same on pine
pine_atr(length) =>
    trueRange = na(high[1])? high-low : max(max(high - low, abs(high - close[1])), abs(low - close[1]))
    //true range can be also calculated with tr(true)
    rma(trueRange, length)

plot(pine_atr(14))


plot(rma(close, 15))

//the same on pine
pine_rma(src, length) =>
    alpha = 1/length
    sum = 0.0
    sum := na(sum[1]) ? sma(src, length) : alpha * src + (1 - alpha) * nz(sum[1])
plot(pine_rma(close, 15))



--------------------------------------------------------------------------------------------------


HL = pd.DataFrame(abs(data['high'] - data['low']))
HCp = pd.DataFrame(abs(data['high'] - data['close'].shift(1)))
LCp = pd.DataFrame(abs(data['low'] - data['close'].shift(1)))

tr = pd.concat([HL, HCp, LCp], axis = 1, join = 'inner').max(axis = 1)

HHp = data['high'] - data['high'].shift(1)
LLp = data['low'] - data['low'].shift(1)

def plus_dm(HHp, LLp):
    if HHp > LLp:
        if HHp > 0:
            # plus_di = HHp
            return 
        else:
            # plus_di = 0
            return 0


def minus_dm(HHp, LLp):
    if -LLp > HHp:
        if -LLp > 0:
            # minus_di = -LLp
            return -LLp
        else:
            # minus_di = 0
            return 0


plus_di  = plus_di(HHp, LLp)
minus_di = minus_di(HHp, LLp)

if plus_di > minus_di:
    plus_di = HHp
    minus_di = 0

if plus_di < minus_di:
    plus_di = 0
    minus_di = -LLp





H-Hp < Lp-l


H   L
3   2
7   5


pdm = h-ph
ndm = pl-l

if (pdm > ndm) and (pdm > 0):
    return pdm
else:
    return 0


if (ndm > pdm) and (ndm > 0) :
    return ndm
else:
    return 0

pdm_n = pdm_n