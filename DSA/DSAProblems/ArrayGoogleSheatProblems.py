
# # https://www.geeksforgeeks.org/dsa/maximum-and-minimum-in-an-array/

# def maximumAndMinimumOfArray(array):
#     """
#     Maximum and minimum of an array using minimum number of comparisons
#     # 
#     comparision = 2n - 2
#     """
#     current_min = array[0]
#     current_max = array[0]
#     # 
#     for element in array :
#         if element < current_min:
#             current_min = element
#         elif element > current_max:
#             current_max = element
#     # 
#     return current_min, current_max


# def maximumAndMinimumOfArray(array):
#     """
#     comparision = 1.5n - 2
#     # 
#     1st comparison → in the while loop condition → but it's just checking loop index, not a data comparison → ❌ not counted
#     2nd comparison → if arr[i] > arr[i+1] → ✅ counted (pairwise)
#     3rd comparison → max(...) → ✅ counted
#     4th comparison → min(...) → ✅ counted
#     """
#     n = len(array)
#     # 
#     if n % 2 == 0:
#         if array[0] > array[1]:
#             current_min = array[1]
#             current_max = array[0]
#         else:
#             current_min = array[0]
#             current_max = array[1]
#         # 
#         i = 2
#     else:
#         current_min = current_max = array[0]
#         i = 1
#     # 
#     while i < n-1:
#         if array[i] > array[i+1]:
#             current_min = min(current_min, array[i+1])
#             current_max = max(current_max, array[i])
#         # 
#         else:
#             current_min = min(current_min, array[i])
#             current_max = max(current_max, array[i+1])
#         # 
#         i += 2
#         print(current_min, current_max)
#     # 
#     return current_min, current_max


# # -------------------------------------------------------------------------------------------------


# # https://www.geeksforgeeks.org/dsa/program-to-reverse-an-array/

# def arrayReverse(array):
#     """
#     Using a temporary array - O(n) Time and O(n) Space
#     """
#     n = len(array)-1
#     temp_array = []
#     # 
#     while n > -1:
#         temp_array.append(array[n])
#         n -= 1
#     # 
#     return temp_array


# def arrayReverse(array):
#     """
#     By Swapping Elements - O(n) Time and O(1) Space
#     this program is correct but it has many steps
#     """
#     def evenArrayReverse(array, length):
#         """
#         """
#         temp = None
#         inital_index = 0
#         final_index = length-1
#         # 
#         for i in range(0, int(length/2)):
#             temp = array[i]
#             array[inital_index] = array[final_index]
#             array[final_index] = temp
#             # 
#             inital_index += 1
#             final_index -= 1
#         # 
#         return array
#     # 
#     def oddArrayReverse(array, length):
#         """
#         """
#         temp = None
#         inital_index = 0
#         final_index = length-1
#         # 
#         for i in range(0, int(length/2)):
#             temp = array[i]
#             array[inital_index] = array[final_index]
#             array[final_index] = temp
#             # 
#             inital_index += 1
#             final_index -= 1
#         # 
#         return array
#     # 
#     n = len(array)
#     if n % 2:
#         return evenArrayReverse(array=array, length=n)
#     else:
#         return oddArrayReverse(array=array, length=n)


# def arrayReverse(array):
#     """
#     By Swapping Elements - O(n) Time and O(1) Space
#     this program is correct but it has less step
#     """
#     n = len(array)
#     mid = n // 2 
#     for i in range(0, mid):
#         temp = array[i]
#         array[i] = array[n-i-1]
#         array[n-i-1] = temp
#     # 
#     return array


# # -------------------------------------------------------------------------------------------------


# def maxSubArray(self, nums):
#     """
#     find the continous sub array having maximum sum
#     Kadane’s Algorithm
#         1. start a new sub array
#         2. extend subarray
#     """
#     max_current = max_global = nums[0]
#     # 
#     for i in range(1, len(nums)):
#         max_current = max(nums[i], max_current + nums[i]) # condition - start a new sub array / extend subarray
#         max_global = max(max_global, max_current)
#     # 
#     return max_global


# # -------------------------------------------------------------------------------------------------


# def containsDuplicate(self, nums):
#     """
#     """
#     nums.sort()
#     prev_item = nums[0]
#     for i in range(1, len(nums)):
#         if prev_item == nums[i]:
#             return True
#         else:
#             prev_item = nums[i]
#     # 
#     return False


# # -------------------------------------------------------------------------------------------------


# def minimizeChocolateDifference(array, m):
#     """
#     Chocolate Distribution Problem
    
#     Given an array arr[] of n integers where arr[i] represents the number of chocolates in ith packet.
#     Each packet can have a variable number of chocolates.
#     There are m students
#     the task is to distribute chocolate packets such that: 
#     Each student gets exactly one packet.
#     The difference between the maximum and minimum number of chocolates in the packets given to the students is minimized.
#     """
#     array.sort()
#     print(array)
#     min_diff = array[-1]
#     for i in range(0, len(array)-m+1):
#         min_diff = min(array[i+m-1] - array[i], min_diff)
#         print(min_diff)
#     # 
#     return min_diff


# # -------------------------------------------------------------------------------------------------


# def search(array, target):
#     """
#     def search(self, array, target):
#     """
#     pivort = searchPivot(array)
#     pivort_index = array.index(pivort)
#     array = array[pivort_index:] + array[:pivort_index]
#     print(array)
#     try:
#         index = array.index(target)
#     except ValueError as e:
#         return -1
#     # 
#     print(index, pivort_index)
#     if index + pivort_index < len(array):
#         return index + pivort_index
#     else :
#         return index + pivort_index - len(array)


# def searchPivot(array):
#     """
#     """
#     print(array)
#     array_len = len(array)
#     # 
#     if array_len == 1 :
#         return array[0]
#     # 
#     elif array_len > 1 :
#         m1, m2 = array_len//2-1, array_len//2
#         # 
#         if array[0] > array[m1]: # first half is unsorted
#             return searchPivot(array=array[:m1+1])
#                 # 
#         # 
#         elif array[m2] > array[-1] : # second half is unsorted
#             return searchPivot(array=array[m2:])
#         # 
#         else : # both are sorted
#             if array[0] < array[m2]:
#                 return array[0]
#             else:
#                 return array[m2]


# # -------------------------------------------------------------------------------------------------


# def nextPermutation(array):
#     """
#     """
#     sub_array = [array[-1]]
#     # 
#     for i in range(2,len(array)+1):
#         # print(i)
#         if array[-i] >= array[1-i]:
#             sub_array.append(array[-i])
#         # 
#         else:
#             sub_array.append(array[-i])
#             sub_array.sort()
#             just_big_num_index = justBigNumIndex(array=sub_array, num=array[-i])
#             just_big_num = sub_array.pop(just_big_num_index)
#             # print(array[:-i] + [just_big_num] + sub_array)
#             return array[:-i] + [just_big_num] + sub_array
#     # 
#     return sub_array


# def justBigNumIndex(array, num):
#     """
#     """
#     num_index = array.index(num)
#     for i in range(num_index+1, len(array)):
#         if array[i] != num:
#             # print("justBigNumIndex :", i, array)
#             return i


# # -------------------------------------------------------------------------------------------------


# def maxProfit(prices):
#     """
#     def maxProfit(self, prices):
#     """
#     min_price = prices[0]
#     max_profit = 0
#     # 
#     for item in prices[1:]:
#         print(item)
#         if item > min_price:
#             max_profit = max(max_profit, item - min_price)
#             print('max_profit : ', max_profit)
#         # 
#         else:
#             min_price = item
#             print('min_price : ', min_price)
#     # 
#     return max_profit


# # -------------------------------------------------------------------------------------------------


# def repeatedNumber(array):
#     """
#     |A-B| = | sigma(n) - array_sum|
#     A/B = array_mult/n!
#     """
#     len_array = len(array)
#     # 
#     sigma_n = sum(range(1, len_array+1))
#     array_sum = sum(array)
#     # 
#     array_mult = 1
#     for item in array:
#         array_mult = item*array_mult
#     # 
#     fact_n = 1
#     for i in range(1, len_array+1):
#         fact_n = i*fact_n
#     # 
#     if array_sum > sigma_n: # A > B
#         x = round(1 - fact_n/array_mult, 4)
#         y = array_sum - sigma_n
#         a = int(y/x)
#         b = int(a - y)
#         return a, b
#     # 
#     else: # A < B
#         x = round(fact_n/array_mult - 1, 4)
#         y = sigma_n - array_sum
#         a = int(y/x)
#         b = int(y + a)
#         return a, b


# # -------------------------------------------------------------------------------------------------


# def findKthLargest(array, k):
#     """
#     """
#     sorted_array = []
#     # 
#     for i in range(1, k+1):
#         max_item = array[0]
#         max_item_index = 0
#         # 
#         for i in range(1, len(array)):
#             if array[i] > max_item:
#                 max_item_index, max_item = i, array[i]
#         # 
#         sorted_array.append(max_item)
#         array.pop(max_item_index)
#     # 
#     return sorted_array[-1]


# # -------------------------------------------------------------------------------------------------


# def trap(array):
#     """
#     """
#     len_array = len(array)
#     # 
#     max_hight = 0
#     max_hight_array = []
#     # 
#     for i in range(0,len_array):
#         if array[i] > max_hight:
#             max_hight = array[i]
#             max_hight_array = [i]
#         # 
#         elif array[i] == max_hight:
#             max_hight_array.append(i)
#     print('max_hight :', max_hight, "max_hight_array", max_hight_array)
#     # 
#     total_volume = max_hight*len_array
#     # 
#     # subtract left blank volume
#     left_blank_volume = max_hight - array[0]
#     temp_hight = array[0]
#     # 
#     for item in array[1:max_hight_array[0]+1]:
#         if item > temp_hight:
#             left_blank_volume += max_hight - item
#             temp_hight = item
#         # 
#         else:
#             left_blank_volume += max_hight - temp_hight
#     # 
#     # subtract right blank volume
#     reverse_array = array[max_hight_array[-1]:]
#     reverse_array.reverse()
#     print(reverse_array)
#     right_blank_volume = max_hight - reverse_array[0]
#     temp_hight = reverse_array[0]
#     # 
#     for item in reverse_array[1:]:
#         if item > temp_hight:
#             right_blank_volume += max_hight - item
#             temp_hight = item
#         # 
#         else:
#             right_blank_volume += max_hight - temp_hight
#     # 
#     print('total_volume : ', total_volume, 'left_blank_volume : ', left_blank_volume, 'right_blank_volume : ', right_blank_volume, 'sum(array) : ', sum(array))
#     return total_volume - left_blank_volume - right_blank_volume - sum(array)


# # # -------------------------------------------------------------------------------------------------


# def productExceptSelf(array):
#     """
#     """
#     if 0 in array:
#         zero_index = array.index(0)
#         temp_array = array.copy()
#         temp_array.pop(zero_index)
#         if 0 not in temp_array:
#             answer_array = []
#             # 
#             total_mult = 1
#             for item in temp_array:
#                 total_mult = total_mult*item
#             # 
#             for item in array:
#                 if item != 0:
#                     answer_array.append(0)
#                 else:
#                     answer_array.append(total_mult)
#             # 
#             return answer_array
#         else:
#             answer_array = []
#             # 
#             for i in range(0,len(array)):
#                 answer_array.append(0)
#             # 
#             return answer_array
#     # 
#     else:
#         answer_array = []
#         # 
#         total_mult = 1
#         for item in array:
#             total_mult = total_mult*item
#         # 
#         for item in array:
#             answer_array.append(total_mult//item)
#         # 
#         return answer_array


# def productExceptSelf(nums):
#     n = len(nums)
#     answer = [1] * n
    
#     # Step 1: Prefix product
#     prefix = 1
#     for i in range(n):
#         answer[i] = prefix
#         prefix *= nums[i]
#         # 
#     # Step 2: Suffix product
#     suffix = 1
#     for i in range(n - 1, -1, -1):
#         answer[i] *= suffix
#         suffix *= nums[i]
#         # 
#     return answer


# -------------------------------------------------------------------------------------------------


# def maxProduct(nums):
#     if not nums:
#         return 0
#     # 
#     max_so_far = min_so_far = result = nums[0]
#     # 
#     for i in range(1, len(nums)):
#         curr = nums[i]
#         temp_max = max(curr, curr * max_so_far, curr * min_so_far)
#         temp_min = min(curr, curr * max_so_far, curr * min_so_far)
#         # 
#         max_so_far = temp_max
#         min_so_far = temp_min
#         # 
#         result = max(result, max_so_far)
#     # 
#     return result


# # -------------------------------------------------------------------------------------------------


# def searchPivot(array):
#     """
#     https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#     """
#     print(array)
#     array_len = len(array)
#     # 
#     if array_len == 1 :
#         return array[0]
#     # 
#     elif array_len > 1 :
#         m1, m2 = array_len//2-1, array_len//2
#         # 
#         if array[0] > array[m1]: # first half is unsorted
#             return searchPivot(array=array[:m1+1])
#                 # 
#         # 
#         elif array[m2] > array[-1] : # second half is unsorted
#             return searchPivot(array=array[m2:])
#         # 
#         else : # both are sorted
#             if array[0] < array[m2]:
#                 return array[0]
#             else:
#                 return array[m2]


# # -------------------------------------------------------------------------------------------------


# def PairSumINSortedAndRotatedArray(array, target):
#     """
#     """
#     pivot = searchPivot(array=array)
#     pivot_index = array.index(pivot)
#     array = array[pivot_index:] + array[:pivot_index]
#     print(array)
#     # 
#     left_pointer = 0
#     right_pointer = len(array) - 1
#     # 
#     while left_pointer <= right_pointer:
#         pointer_sum = array[left_pointer] + array[right_pointer]
#         print(pointer_sum)
#         if pointer_sum > target:
#             right_pointer -= 1
#             continue
#         # 
#         elif pointer_sum < target:
#             left_pointer += 1
#             continue
#         # 
#         else :
#             return True

#     # 
#     return False


# def searchPivot(array):
#     """
#     https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#     """
#     print(array)
#     array_len = len(array)
#     # 
#     if array_len == 1 :
#         return array[0]
#     # 
#     elif array_len > 1 :
#         m1, m2 = array_len//2-1, array_len//2
#         # 
#         if array[0] > array[m1]: # first half is unsorted
#             return searchPivot(array=array[:m1+1])
#                 # 
#         # 
#         elif array[m2] > array[-1] : # second half is unsorted
#             return searchPivot(array=array[m2:])
#         # 
#         else : # both are sorted
#             if array[0] < array[m2]:
#                 return array[0]
#             else:
#                 return array[m2]


# # -------------------------------------------------------------------------------------------------


# def threeSum(array):
#     nums.sort()
#     result = []
#     # 
#     for i in range(len(nums)):
#         # Skip duplicate values for the first element
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue
#         # 
#         target = -nums[i]
#         left = i + 1
#         right = len(nums) - 1
#         # 
#         while left < right:
#             total = nums[left] + nums[right]
#             if total == target:
#                 result.append([nums[i], nums[left], nums[right]])
#                 left += 1
#                 right -= 1
#                 # Skip duplicates for second and third elements
#                 while left < right and nums[left] == nums[left - 1]:
#                     left += 1
#                 while left < right and nums[right] == nums[right + 1]:
#                     right -= 1
#             elif total < target:
#                 left += 1
#             else:
#                 right -= 1
#     # 
#     return result


# # -------------------------------------------------------------------------------------------------


# def maxArea(array):
#     """
#     """
#     max_area = 0
#     # 
#     left = 0
#     right = len(array)-1
#     while left < right:
#         max_area = max(max_area, (right-left)*min(array[left], array[right]))
#         # 
#         if array[left] < array[right]:
#             left += 1
#         # 
#         else:
#             right -= 1
#     # 
#     return max_area


# # -------------------------------------------------------------------------------------------------


# def kthSmallest(array, k):
#     """
#     """
#     sorted_array = []
#     # 
#     for i in range(1, k+1):
#         min_item = array[0]
#         min_item_index = 0
#         # 
#         for i in range(1, len(array)):
#             if array[i] < min_item:
#                 min_item_index, min_item = i, array[i]
#         # 
#         sorted_array.append(min_item)
#         array.pop(min_item_index)
#     # 
#     return sorted_array[-1]


# # -------------------------------------------------------------------------------------------------


def mergeOverlappingIntervals(array):
    """
    """
    array.sort()
    # 
    start   = array[0][0]
    end     = array[0][1]
    interval_array = []
    # 
    for item in array[1:]:
        if item[0] < end:
            end = max(end, item[1])
        else:
            interval_array.append([start, end])
            start   = item[0]
            end     = item[1]
    # 
    interval_array.append([start, end])
    # 
    return interval_array


# # -------------------------------------------------------------------------------------------------


# def makeArayPalindrome(array):
#     """
#     """
#     left    = 0
#     right   = len(array)-1
#     # 
#     left_item   = array[left]
#     right_item  = array[right]
#     # 
#     merge = 0
#     # 
#     while left < right:
#         if left_item < right_item:
#             left += 1
#             merge += 1
#             left_item += array[left]
#         # 
#         elif left_item > right_item:
#             merge += 1
#             right -= 1
#             right_item += array[right]
#         else:
#             left += 1
#             right -= 1
#             left_item = array[left]
#             right_item = array[right]
#     # 
#     return merge


# # -------------------------------------------------------------------------------------------------


# def formBiggestNumber(array):
#     """
#     """
#     str_array = []
#     for item in array:
#         str_array.append(str(item))
#     # 
#     str_array.sort()
#     str_array.reverse()
#     print(str_array)
#     # 
#     max_str =''
#     pointer_1 = str_array[0]
#     pointer_2 = str_array[1]
#     for item in str_array[2:] + ['0','0']:
#         print(max_str)
#         if int(pointer_1 + pointer_2) >= int(pointer_2 + pointer_1):
#             max_str += pointer_1
#             pointer_1 = item
#         # 
#         else:
#             max_str += pointer_2
#             pointer_2 = item
#     # 
#     return max_str


# # -------------------------------------------------------------------------------------------------


# Space optimization using bit manipulations
# not solving this question because it want bit manipulations concept which has question down in sheet
# so i will understand and use bit manipulations concept later


# # -------------------------------------------------------------------------------------------------


# def longestSubarrayDivK(array, k):
#     """
#     concept:
#     1. summing array element from fist to last and calculate its remender
#     2. if that remender occour in past means the sum between past ocuurance and this occurance is a multiple of k
#     3. save fist and last occurance in dict
#     4. at last calculate the max diffrence between first and last occurance of every remender
#     """
#     len_array = len(array)
#     rmd_dict = {}
#     sum = 0
#     # 
#     for i in range(0,len_array):
#         sum += array[i]
#         rmd = sum % k
#         # 
#         if rmd not in rmd_dict:
#            rmd_dict[rmd] = [i, i]
#         # 
#         else:
#             rmd_dict[rmd][1] = i
#     # 
#     max_subarray_len = 0
#     for key in list(rmd_dict.keys()):
#         max_subarray_len = max(max_subarray_len, rmd_dict[key][1] - rmd_dict[key][0])
#     # 
#     return max_subarray_len


# # -------------------------------------------------------------------------------------------------


# def findCombination(array, r):
#     """
#     """
#     # convert elements to string
#     str_array = []
#     for item in array:
#         str_array.append(str(item))
#     # 
#     return recursiveFinding(array=str_array,r=r)


# def recursiveFinding(array,r):
#     """
#     """
#     # print('initiate - array : ', array, 'r : ', r)
#     if r == 1:
#         return array
#     # 
#     # r > 1
#     fixed_item = array[0]
#     item_list = []
#     for i in range(1, len(array)):
#         # print('internal array : ', array[i:],'r : ', r-1)
#         rf = recursiveFinding(array[i:],r-1)
#         # print('rf : ', rf)
#         for item in rf:
#             item_list.append(fixed_item + item)
#         # 
#         fixed_item = array[i]
#     # 
#     # print(item_list)
#     return item_list

