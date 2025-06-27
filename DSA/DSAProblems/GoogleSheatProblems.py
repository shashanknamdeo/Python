
# https://www.geeksforgeeks.org/dsa/maximum-and-minimum-in-an-array/

def maximumAndMinimumOfArray(array):
    """
    Maximum and minimum of an array using minimum number of comparisons
    # 
    comparision = 2n - 2
    """
    current_min = array[0]
    current_max = array[0]
    # 
    for element in array :
        if element < current_min:
            current_min = element
        elif element > current_max:
            current_max = element
    # 
    return current_min, current_max


def maximumAndMinimumOfArray(array):
    """
    comparision = 1.5n - 2
    # 
    1st comparison → in the while loop condition → but it's just checking loop index, not a data comparison → ❌ not counted
    2nd comparison → if arr[i] > arr[i+1] → ✅ counted (pairwise)
    3rd comparison → max(...) → ✅ counted
    4th comparison → min(...) → ✅ counted
    """
    n = len(array)
    # 
    if n % 2 == 0:
        if array[0] > array[1]:
            current_min = array[1]
            current_max = array[0]
        else:
            current_min = array[0]
            current_max = array[1]
        # 
        i = 2
    else:
        current_min = current_max = array[0]
        i = 1
    # 
    while i < n-1:
        if array[i] > array[i+1]:
            current_min = min(current_min, array[i+1])
            current_max = max(current_max, array[i])
        # 
        else:
            current_min = min(current_min, array[i])
            current_max = max(current_max, array[i+1])
        # 
        i += 2
        print(current_min, current_max)
    # 
    return current_min, current_max


# -------------------------------------------------------------------------------------------------


# https://www.geeksforgeeks.org/dsa/program-to-reverse-an-array/

def arrayReverse(array):
    """
    Using a temporary array - O(n) Time and O(n) Space
    """
    n = len(array)-1
    temp_array = []
    # 
    while n > -1:
        temp_array.append(array[n])
        n -= 1
    # 
    return temp_array


def arrayReverse(array):
    """
    By Swapping Elements - O(n) Time and O(1) Space
    this program is correct but it has many steps
    """
    def evenArrayReverse(array, length):
        """
        """
        temp = None
        inital_index = 0
        final_index = length-1
        # 
        for i in range(0, int(length/2)):
            temp = array[i]
            array[inital_index] = array[final_index]
            array[final_index] = temp
            # 
            inital_index += 1
            final_index -= 1
        # 
        return array
    # 
    def oddArrayReverse(array, length):
        """
        """
        temp = None
        inital_index = 0
        final_index = length-1
        # 
        for i in range(0, int(length/2)):
            temp = array[i]
            array[inital_index] = array[final_index]
            array[final_index] = temp
            # 
            inital_index += 1
            final_index -= 1
        # 
        return array
    # 
    n = len(array)
    if n % 2:
        return evenArrayReverse(array=array, length=n)
    else:
        return oddArrayReverse(array=array, length=n)


def arrayReverse(array):
    """
    By Swapping Elements - O(n) Time and O(1) Space
    this program is correct but it has less step
    """
    n = len(array)
    mid = n // 2 
    for i in range(0, mid):
        temp = array[i]
        array[i] = array[n-i-1]
        array[n-i-1] = temp
    # 
    return array


def maxSubArray(self, nums):
    """
    find the continous sub array having maximum sum
    """
init_flag       = False       # express that is there any item in sub string
    for item in nums:


if init_flag == False:
    sub_array       = []
    negetive_sum    = None
    negative_flag   = False   # express that are we incounterd with a negestive sum which is not normalise by positive sum
    # 
    if item < 0 :
        continue
    else :
        init_flag = True
        sub_array.append(item)
# 
else:
    if negative_flag == False:
        if item > 0:
            handelpositiveItem()
        # 
        elif item < 0:
            handelNegativeItem(item=item, negetive_sum=negetive_sum, negative_flag=negative_flag, sub_array=array, init_flag=init_flag)
    # 
    if negative_flag == True:
        handelNegativeItem(item=item, negetive_sum=negetive_sum, negative_flag=negative_flag, sub_array=array, init_flag=init_flag)


def handelpositiveItem(item=item, negetive_sum=negetive_sum, negative_flag=negative_flag, sub_array=array, init_flag=init_flag):
    """
    """
    if negative_flag == False and item > 0:
        sub_array.append(item)
    # 
    elif negative_flag == True:
















def handelNegativeItem(item, negetive_sum, negative_flag, sub_array, init_flag):
    """
    """
    if negative_flag == False :
        if sub_array.sum() + item >= 0 :
            sub_array.append(item)
            negative_flag = True
            negetive_sum = item
        else:
            init_flag = False
            return
    # 
    else:
        if sub_array.sum() + item < 0:
            init_flag = False
            return
        else:





1,2,-2,1,-1



# devide and conquer menthord
#     divide the arrray in single element substring
#     if add subarray  to other is make the the sum grater than add it
#     otherwise left it


def maxSubArray(self, nums):
    """
    find the continous sub array having maximum sum
    Divide and Conquer
    """




def getLargestSumSubarray(array):
    """
    """
    # divide
    
    # base case
    if 


hash







