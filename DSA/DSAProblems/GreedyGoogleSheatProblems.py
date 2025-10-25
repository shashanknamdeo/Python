def startStation(self, gas, cost):
    """
    https://www.geeksforgeeks.org/problems/circular-tour-1587115620/1
    """

# -------------------------------------------------------------------------------------------------

def activitySelection(start, finish):
    """
    """
    activity = sorted(zip(start, finish), key=lambda x: x[1])
    # 
    max_activity = 1
    prev_finish = activity[0][1]
    # 
    for s, f in activity[1:]:
        if s > prev_finish:
            max_activity += 1
            prev_finish = f
    # 
    return max_activity


# -------------------------------------------------------------------------------------------------

def findMin(n):
    """
    """
    coins = [1,2,5,10]
    coin = coins.pop()
    number = 0
    # 
    while n != 0:
        if coin <= n:
            n -= coin
            number += 1
        else:
            coin = coins.pop()
    # 
    return number


# -------------------------------------------------------------------------------------------------

def minSum(arr, n):
    """
    """
    if n == 0:
        return 0
    elif n == 1:
        return array[0]
    # 
    array.sort()
    array.reverse()
    f = ''
    s = ''
    # 
    flag = True
    while array:
        if flag == True:
            f += str(array.pop())
        else:
            s += str(array.pop())
        flag = not flag
    # 
    return int(f) + int(s)


# array = [6, 8, 4, 5, 2, 3]

array = [5, 3, 0, 7, 4]






print(minSum(arr=array, n=len(array)))

# df = activitySelection(start, finish)