
# def isPossible(self, k, array_1, array_2):
#     """
#     """
#     if len(array_1) != len(array_2):
#         return False
#     # 
#     array_1.sort()
#     array_2.sort()
#     array_2.reverse()
#     # 
#     for i in range(0, len(array_1)):
#         if array_1[i] + array_2[i] < k:
#             return False
#     # 
#     return True

# # -------------------------------------------------------------------------------------------------


# def countSort(string):
#     """
#     def countSort(self,string):
#     """
#     alphabet_map = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
#     'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
#     # 
#     count_array = [0] * 27
#     # 
#     for item in string:
#         count_array[alphabet_map[item]] += 1
#     # 
#     for i in range(1, 27):
#         count_i1 = count_i1 + count_array[i-1]
#     # 
#     print(count_array)
#     answer_list = ['#'] * count_array[-1]
#     # 
#     for i in range(len(string)-1, -1, -1):
#         char = string[i]
#         char_count = count_array[alphabet_map[char]]
#         # print(char_count)
#         answer_list[char_count - 1] = char
#         count_array[alphabet_map[char]] = char_count - 1
#     # 
#     return "".join(answer_list)

# # -------------------------------------------------------------------------------------------------


# def commonElements(array_1, array_2, array_3):
#         """
#         """
#         if not array_1 or not array_2 or not array_3:
#             return [-1]
#         # 
#         array_1 = getUniqueItemArray(array=array_1)
#         array_2 = getUniqueItemArray(array=array_2)
#         array_3 = getUniqueItemArray(array=array_3)
#         # 
#         common_array_12 = commonElementsOf2Array(array_1=array_1, array_2=array_2)
#         common_array_23 = commonElementsOf2Array(array_1=array_2, array_2=array_3)
#         # 
#         if not common_array_12 or not common_array_23:
#             return [-1]
#         #
#         common_array_12.reverse()
#         common_array_23.reverse()
#         common_array = commonElementsOf2Array(array_1=common_array_12, array_2=common_array_23)
#         # 
#         if not  common_array:
#             return [-1]
#         # 
#         common_array.reverse()
#         return common_array


# def getUniqueItemArray(array):
#     """
#     """
#     last_item = array[0]
#     final_array = [last_item]
#     for item in array[1:]:
#         if item != last_item:
#             final_array.append(item)
#             last_item = item
#     # 
#     return final_array


# def commonElementsOf2Array(array_1, array_2):
#     """
#     """
#     array_1, array_2 = array_1[:], array_2[:]
#     if not array_1 and not array_2:
#         return -1
#     # 
#     # print(array_1)
#     # print(array_2)
#     # 
#     common_array = []
#     # 
#     while array_1 and array_2:
#         temp_element_array_1 = array_1[-1]
#         temp_element_array_2 = array_2[-1]
#         # 
#         # print(temp_element_array_1, temp_element_array_2)
#         if temp_element_array_1 ==  temp_element_array_2:
#             common_array.append(temp_element_array_1)
#             array_1.pop()
#             array_2.pop()
#         #
#         elif temp_element_array_1 > temp_element_array_2:
#             array_1.pop()
#         elif temp_element_array_1 < temp_element_array_2:
#             array_2.pop()
#     # 
#     # print(common_array)
#     return common_array

# # -------------------------------------------------------------------------------------------------

# import math

# def findStepKeyIndex(array, k, x):
#     """
#     def findStepKeyIndex(self, arr, k, x):
#     """
#     if not array:
#         return -1
#     # 
#     n = len(arr)
#     # 
#     i = 0
#     while i < n:
#         if arr[i] == x:
#             return i
#         # 
#         diff = abs(arr[i] - x)
#         # 
#         jump = max(1, diff // k)
#         # 
#         i += jump
#     # 
#     return -1

# -------------------------------------------------------------------------------------------------


def findCeil(array, x):
    """
    """
    n = len(arr)
    if n == 0:
        return -1
    # 
    if x > arr[n - 1]:
        return -1
    # 
    low, high = 0, n - 1
    result_index = -1
    # 
    while low <= high:
        mid = low + (high - low) // 2
        # 
        if arr[mid] >= x:
            result_index = mid
            high = mid - 1
        # 
        else:
            low = mid + 1
    # 
    return result_index



from typing import List

def findPair( array: List[int], x: int) -> int:
    """
    """
    if not array:
        return False
    # 
    array.sort()
    print(array)
    # 
    i = 0
    j = len(array) - 1
    # 
    if x > array[j] - array[i]:
        return False
    # 
    while i < j:
        i1 = array[i]
        i2 = array[i+1]
        j1 = array[j]
        j2 = array[j-1]
        # 
        print(i1, i2, j1, j2)
        diff = j1 - i1
        if diff == x:
            return True
        elif diff < x:
            return False
        # 
        if i2 - i1 <= j1 - j2:
            i += 1
        elif i2 - i1 > j1 - j2:
            j -= 1
    # 
    return False




class Solution:
    def findPair( array: List[int], x: int) -> int:
        """
        """
        if not array:
            return False
        # 
        len_array = len(array)
        array.sort()
        # print(array)
        # 
        j = 1
        # 
        for i in range(0, len_array):
            while j < len_array and array[j] - array[i] < x:
                j += 1
            # 
            if j < len_array and i != j and array[j] - array[i] == x:
                return True
        # 
        return False





# -------------------------------------------------------------------------------------------------

# array = [1, 2, 8, 10, 11, 12, 19]
# x = 5

array = [1, 10, 1, 1, 7, 2]

x = 8

print(findPair(array, x))










































"""
https://www.geeksforgeeks.org/dsa/merge-sort-for-linked-list/
https://www.geeksforgeeks.org/dsa/quicksort-on-singly-linked-list/
sorting algorithms:
    merge
    quick
    heap
    etc
searching algorithms:
    binary search
    etc
"""