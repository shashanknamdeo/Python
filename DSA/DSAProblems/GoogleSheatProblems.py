
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
    Kadane’s Algorithm
        1. start a new sub array
        2. extend subarray
    """
    def maxSubArray(self, nums):
        max_current = max_global = nums[0]
        # 
        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current + nums[i]) # condition - start a new sub array / extend subarray
            max_global = max(max_global, max_current)
        # 
        return max_global


def containsDuplicate(self, nums):
    """
    """
    nums.sort()
    prev_item = nums[0]
    for i in range(1, len(nums)):
        if prev_item == nums[i]:
            return True
        else:
            prev_item = nums[i]
    # 
    return False


def minimizeChocolateDifference(array, m):
    """
    Chocolate Distribution Problem
    
    Given an array arr[] of n integers where arr[i] represents the number of chocolates in ith packet.
    Each packet can have a variable number of chocolates.
    There are m students
    the task is to distribute chocolate packets such that: 
    Each student gets exactly one packet.
    The difference between the maximum and minimum number of chocolates in the packets given to the students is minimized.
    """
    array.sort()
    print(array)
    min_diff = array[-1]
    for i in range(0, len(array)-m+1):
        min_diff = min(array[i+m-1] - array[i], min_diff)
        print(min_diff)
    # 
    return min_diff


def search(array, target):
    """
    def search(self, array, target):
    """
    pivort = searchPivot(array)
    pivort_index = array.index(pivort)
    array = array[pivort_index:] + array[:pivort_index]
    print(array)
    try:
        index = array.index(target)
    except ValueError as e:
        return -1
    # 
    print(index, pivort_index)
    if index + pivort_index < len(array):
        return index + pivort_index
    else :
        return index + pivort_index - len(array)


def searchPivot(array):
    """
    """
    print(array)
    array_len = len(array)
    # 
    if array_len == 1 :
        return array[0]
    # 
    elif array_len > 1 :
        m1, m2 = array_len//2-1, array_len//2
        # 
        if array[0] > array[m1]: # first half is unsorted
            return searchPivot(array=array[:m1+1])
                # 
        # 
        elif array[m2] > array[-1] : # second half is unsorted
            return searchPivot(array=array[m2:])
        # 
        else : # both are sorted
            if array[0] < array[m2]:
                return array[0]
            else:
                return array[m2]



def nextPermutation(array):
    """
    https://leetcode.com/problems/next-permutation/
    nextPermutation(self, nums)
    """
    len_array = len(array)
    # 
    sorted_array = array.copy()
    sorted_array.sort()
    sorted_array.reverse()
    if array == sorted_array:
        array.reverse()
        return array
    # 
    sub_array = [array[-1]]
    for i in range(2,len_array+1):
        if array[-i] > array[1-i]:
            sub_array.append(array[-i])
        else:
            sub_array.append(array[-i])
            sub_array.sort()
            just_big_num = sub_array[1+sub_array.index(array[-i])]
            print(sub_array, 1+sub_array.index(array[-i]))
            sub_array.pop(1+sub_array.index(array[-i]))
            return array[:-i] + [just_big_num] + sub_array




123
132