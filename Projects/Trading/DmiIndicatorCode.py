import pandas as pd

def calculate_dmi(data, period=14, verbose=0):
    high = data['High']
    low = data['Low']
    close = data['Close']
    #
    high_diff = high.diff()
    print(high_diff) if verbose >=1 else None
    low_diff = low.diff()
    print(low_diff) if verbose >=1 else None
    #
    print(high - close.shift(1)) if verbose >=1 else None
    tr = pd.DataFrame({
        'HL': high - low,
        'HCp': (high - close.shift(1)).abs(),
        'LCp': (low - close.shift(1)).abs()
    })
    #
    tr = tr.max(axis=1)
    #
    tr_smoothed = tr.rolling(window=period).mean()
    pdi = 100 * (tr_smoothed / tr_smoothed.rolling(window=period).sum())
    #
    high_diff_positive = (high_diff > 0).astype(int)
    low_diff_positive = (low_diff > 0).astype(int)
    #
    pdm = 100 * (high_diff_positive * high_diff / tr_smoothed)
    ndm = 100 * (low_diff_positive * low_diff / tr_smoothed)
    #
    pdm_smoothed = pdm.rolling(window=period).mean()
    ndm_smoothed = ndm.rolling(window=period).mean()
    #
    pdi_smoothed = pd.Series(pdi).rolling(window=period).mean()
    mdi = 100 * (ndm_smoothed / pdi_smoothed)
    #
    dmi = pd.DataFrame({'+DI': pdi_smoothed, '-DI': mdi})
        #
    return dmi

# Example usage:
data = pd.DataFrame({
    'High': [142.75, 144.38, 145.63, 144.85, 145.79, 145.75, 144.85, 143.77, 142.89, 141.68, 142.49, 142.54],
    'Low': [140.36, 142.85, 143.23, 142.42, 143.43, 144.12, 142.01, 141.35, 141.12, 139.61, 141.57, 141.37],
    'Close': [141.55, 143.03, 144.47, 143.51, 144.18, 145.71, 143.56, 142.43, 141.61, 140.28, 142.45, 142.11]
})

dmi_result = calculate_dmi(data)
print(dmi_result)
