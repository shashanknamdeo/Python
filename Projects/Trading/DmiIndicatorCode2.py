import numpy as np

def directional_movement_index(high, low, lensig=14, len=14):
    up = np.diff(high)
    down = -np.diff(low)
    plusDM = np.where((up > down) & (up > 0), up, 0)
    minusDM = np.where((down > up) & (down > 0), down, 0)
    
    trur = np.convolve(np.abs(high - low), np.ones(len), mode='valid')
    plus = np.convolve(plusDM, np.ones(len), mode='valid') / trur * 100
    minus = np.convolve(minusDM, np.ones(len), mode='valid') / trur * 100
    
    sum = plus + minus
    adx = np.convolve(np.abs(plus - minus) / np.where(sum == 0, 1, sum), np.ones(lensig), mode='valid') * 100
    
    return adx, plus, minus

# Example usage
high = np.array([142.75, 144.38, 145.63, 144.85, 145.79, 145.75, 144.85, 143.77, 142.89, 141.68, 142.49, 142.54])  # Replace with your high price data
low = np.array([140.36, 142.85, 143.23, 142.42, 143.43, 144.12, 142.01, 141.35, 141.12, 139.61, 141.57, 141.37])   # Replace with your low price data

adx, plus, minus = directional_movement_index(high, low)

# Now you can use the adx, plus, and minus arrays as needed
print("ADX:", adx)
print("+DI:", plus)
print("-DI:", minus)
