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


# -------------------------------------------------------------------------------------------------

def findMinSum(array_1,array_2,n):
    """
    """
    array_1.sort()
    array_2.sort()
    # 
    # print(array_1, array_2)
    min_sum = 0
    for i in range(0, n):
        min_sum += abs(array_1[i] - array_2[i])
        # print(min_sum)
    # 
    return min_sum


# -------------------------------------------------------------------------------------------------

def minCost(coin, n, k): 
    """
    """
    coin.sort()
    # 
    price = 0
    # 
    while coin:
        price += coin.pop(0)
        temp = k
        while temp and coin:
            coin.pop()
            temp -= 1
    # 
    return price


# -------------------------------------------------------------------------------------------------

def nextStack(stack_number):
    stack_number += 1
    if stack_number == 4:
        return 1
    if stack_number == 5:
        return 2
    return stack_number


# def maxEqualSum(n1, n2, n3, s1, s2 , s3):
#     """
#     """
#     # 
#     def stackOperation(stack_number, stack_dict):
#         stack_number = nextStack(stack_number=stack_number)
#         stack_dict[stack_number][1] += stack_dict[stack_number][0].pop()
#         return stack_number, stack_dict
#     # 
#     stack_number = 0
#     max_equal_sum = 0
#     stack_dict = {1 : [s1, 0], 2 : [s2, 0], 3 : [s3, 0]}
#     # 
#     while s1 or s2 or s3:
#         stack_number, stack_dict = stackOperation(stack_number=stack_number, stack_dict=stack_dict)
#         print(stack_number)
#         # 
#         if stack_dict[1][1] == stack_dict[2][1] and stack_dict[1][1] == stack_dict[3][1]:
#             max_equal_sum = stack_dict[1][1]
#         # 
#         if stack_dict[stack_number][1] >= stack_dict[nextStack(stack_number)][1] and stack_dict[stack_number][1] >= stack_dict[nextStack(stack_number+1)][1]:
#             continue
#         # 
#         stack_number -= 1
#     # 
#     return max_equal_sum


def maxEqualSum(n1, n2, n3, s1, s2 , s3):
    """
    """
    print(n1, n2, n3, s1, s2 , s3)
    if not s1 or not  s2 or not  s3:
        return 0
    # 
    temp_max = s1.pop()
    max_equal_sum = 0
    stack_number = 1
    stack_dict = {1 : [s1, temp_max], 2 : [s2, 0], 3 : [s3, 0]}
    # 
    while s1 or s2 or s3:
        stack_number = nextStack(stack_number)
        stack       = stack_dict[stack_number][0]
        stack_sum   = stack_dict[stack_number][1]
        print(temp_max, stack_number, stack, stack_sum)
        # 
        if stack and (stack_sum < temp_max or (stack_dict[1][1] == stack_dict[2][1] and stack_dict[1][1] == stack_dict[3][1])):
            stack_sum += stack.pop()
            temp_max = max(temp_max, stack_sum)
            stack_dict[stack_number][0] = stack       
            stack_dict[stack_number][1] = stack_sum   
        # 
        elif not stack and stack_sum < temp_max:
            print('break : ', stack_number)
            break
        # 
        if stack_dict[1][1] == stack_dict[2][1] and stack_dict[1][1] == stack_dict[3][1]:
            max_equal_sum = stack_dict[1][1]

        # 
    # 
    print(stack_dict)
    return max_equal_sum










s1 = [3, 4]
s2 = [1, 1, 5]
s3 = [7]



n1=n2=n3=0

print(maxEqualSum(n1, n2, n3, s1, s2 , s3))

# df = activitySelection(start, finish)

def maxLevel(boxes, n):
    """
    https://www.geeksforgeeks.org/dsa/find-maximum-height-pyramid-from-the-given-array-of-objects/
    """