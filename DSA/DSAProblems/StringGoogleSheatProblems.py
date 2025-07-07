
# https://docs.google.com/spreadsheets/d/1hXserPuxVoWMG9Hs7y8wVdRCJTcj3xMBAEYUOXQ5Xag/edit?gid=0#gid=0

# last date 6

# def clean_string(string):
#     result = ''
#     for char in string:
#         if char.isalpha() or char.isnumeric():  # keeps only A-Z and a-z
#             result += char
#     return result


# def isPalindrome(string):
#     """
#     """
#     string = clean_string(string=string)
#     string = string.lower()
#     len_string = len(string)
#     # 
#     left  = 0
#     right = len_string -1
#     # 
#     while left < right:
#         if string[left] == string[right]:
#             left  += 1
#             right -= 1
#         else:
#             return False
#     # 
#     return True


# # -------------------------------------------------------------------------------------------------


# def isAnagram(s, t):
#     """
#     """
#     s = sorted(s)
#     t = sorted(t)
#     # 
#     if len(s) != len(t):
#         return False
#     # 
#     for i in range(0, len(s)):
#         if s[i] != t[i]:
#             return False
#     # 
#     return True


# # -------------------------------------------------------------------------------------------------


# def isValid(string):
#     """
#     """
#     if string == '':
#         return True
#     # 
#     parenthes_stack = []
#     parenthes_dict = {'(':')','{':'}','[':']'}
#     keys = parenthes_dict.keys()
#     values = parenthes_dict.values()
#     # 
#     for s in string:
#         if s in keys:
#             parenthes_stack.append(s)
#         elif s in values:
#             if len(parenthes_stack) == 0 or s != parenthes_dict[parenthes_stack.pop()]:
#                 return False
#     # 
#     if len(parenthes_stack) == 0:
#         return True
#     else:
#         return False


# # -------------------------------------------------------------------------------------------------


# def removeConsecutiveCharacter(string):
#     """
#     """
#     new_string = string[0]
#     last_s = string[0]
#     for s in string[1:]:
#         if s != last_s:
#             new_string += s
#             last_s = s
#     # 
#     return new_string


# # -------------------------------------------------------------------------------------------------


# def longestCommonPrefix(array):
#     """
#     """
#     common_prefix = ''
#     index = 0
#     try:
#         s = array[1][0]
#         # 
#         while index >= 0:
#             for string in array:
#                 print(string)
#                 if s != string[index]:
#                     return common_prefix
#             index += 1
#             common_prefix += s
#             s = array[0][index]
#             #
#         # 
#         return common_prefix
#     except IndexError:
#         return common_prefix


# # -------------------------------------------------------------------------------------------------


# def printSequence(arr, input):
#     """
#     str = ["2", "22", "222",
#         "3", "33", "333",
#         "4", "44", "444",
#         "5", "55", "555",
#         "6", "66", "666",
#         "7", "77", "777", "7777",
#         "8", "88", "888",
#         "9", "99", "999", "9999"]
#     1. make dict having A-Z having str values
#     2. iterate over input and get numeric value from dict and append it to output string
#     """


# # -------------------------------------------------------------------------------------------------


# def printDuplicates(s):
#     """
#     1. using Counter, count number of occurance of character in string
#     2. iterate the dict and return character has more than 1 occurance
#     """


# # -------------------------------------------------------------------------------------------------


# def lengthOfLongestSubstring(string):
#     """
#     """
#     char_dict = {}
#     max_string = 0
#     current_string = []
#     # 
#     for char in string:
#         # print(char)
#         value = char_dict.get(char, 0) + 1
#         if value == 2:
#             if max_string < len(current_string):
#                 max_string = len(current_string)
#             # 
#             current_string = current_string[current_string.index(char)+1:]
#             current_string.append(char)
#             char_dict = {c : 1 for c in current_string}
#         # 
#         else :
#             char_dict[char] = value
#             current_string.append(char)
#         # 
#         # print('max_string : ', max_string, 'current_string : ', current_string)
#     # 
#     if max_string < len(current_string):
#                 return len(current_string)
#     # 
#     return max_string


# # -------------------------------------------------------------------------------------------------

# from collections import defaultdict


# def characterReplacement(s, k):
#     # 
#     count = defaultdict(int)
#     max_count = 0  # max freq of a single character in the current window
#     left = 0
#     result = 0
#     # 
#     for right in range(len(s)):
#         count[s[right]] += 1
#         max_count = max(max_count, count[s[right]])
#         # 
#         # If window is invalid (more than k changes needed), shrink from left
#         if (right - left + 1) - max_count > k:
#             count[s[left]] -= 1
#             left += 1
#             # 
#         result = max(result, right - left + 1)
#         # 
#     return result


# # -------------------------------------------------------------------------------------------------

# from collections import defaultdict

# def groupAnagrams(string_list):
#     """
#     """
#     group_dict = defaultdict(list)
#     # 
#     for item in string_list:
#         sorted_item = ''.join(sorted(item))
#         # print('group_dict[sorted_item] : ', group_dict[sorted_item])
#         group_dict[sorted_item] = group_dict[sorted_item] + [item]
#     # 
#     return list(group_dict.values())


# # -------------------------------------------------------------------------------------------------


# def longestPalindrome(s):
#     if not s:
#         return ""
#     # 
#     start, end = 0, 0
#     # 
#     def expand(left, right):
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             left -= 1
#             right += 1
#         return left + 1, right - 1  # return last valid indices
#     # 
#     for i in range(len(s)):
#         # odd length
#         l1, r1 = expand(i, i)
#         # even length
#         l2, r2 = expand(i, i + 1)
#         # 
#         # update longest if found
#         if r1 - l1 > end - start:
#             start, end = l1, r1
#         if r2 - l2 > end - start:
#             start, end = l2, r2
#     # 
#     return s[start:end + 1]


# # -------------------------------------------------------------------------------------------------


# def countSubstrings(s):
#     """
#     """
#     if len(s) == 0:
#         return 0
#     # 
#     palindrome = 0
#     # 
#     def expand(left, right, palindrome):
        
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             palindrome += 1
#             left -= 1
#             right += 1
#         return palindrome  # return last valid indices
#     # 
#     for i in range(len(s)):
#         # odd length
#         palindrome = expand(i, i, palindrome)
#         # even length
#         palindrome = expand(i, i + 1, palindrome)
#     # 
#     return palindrome


# # -------------------------------------------------------------------------------------------------


# def nextPermutation(array):
#     """
#     Array question already attemped
#     """


# # -------------------------------------------------------------------------------------------------

# def count_palindromic_subsequences(s):
#     """
#     https://www.geeksforgeeks.org/problems/count-palindromic-subsequences/1
#     concept - dinamic programing
#     unable to understand now
#     """
#     n = len(s)
#     dp = [[0] * n for _ in range(n)]
#     # 
#     # Base case: every single character is a palindrome
#     for i in range(n):
#         dp[i][i] = 1
#         # 
#     # Fill dp for substrings of length 2 to n
#     for length in range(2, n + 1):
#         for i in range(n - length + 1):
#             print()
#             print(dp)
#             j = i + length - 1
#             # 
#             if s[i] == s[j]:
#                 dp[i][j] = dp[i + 1][j] + dp[i][j - 1] + 1
#             else:
#                 dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
#                 # 
#     return dp[0][n - 1]


# # -------------------------------------------------------------------------------------------------


# def smallest_window(s1, s2):
#     if not s1 or not s2:
#         return ""
#     # 
#     target_count = Counter(s2)
#     required = len(target_count)  # number of unique characters in s2
#     # 
#     left = 0
#     formed = 0
#     window_count = {}
#     min_len = float('inf')
#     min_window = ""
#     # 
#     for right in range(len(s1)):
#         char = s1[right]
#         window_count[char] = window_count.get(char, 0) + 1
#         # 
#         # if current char matches required freq
#         if char in target_count and window_count[char] == target_count[char]:
#             formed += 1
#         # 
#         # try to shrink the window from the left
#         while left <= right and formed == required:
#             # update result if it's smaller
#             window_size = right - left + 1
#             if window_size < min_len:
#                 min_len = window_size
#                 min_window = s1[left:right + 1]
#             # 
#             # remove leftmost character
#             left_char = s1[left]
#             window_count[left_char] -= 1
#             if left_char in target_count and window_count[left_char] < target_count[left_char]:
#                 formed -= 1
#             left += 1
#     # 
#     return min_window


# # -------------------------------------------------------------------------------------------------


# def match(wild, pattern):
#     """
#     Dynamic programing
#     Unable to solve now
#     """


# # -------------------------------------------------------------------------------------------------


# def longestPrefixSuffix(string):
#     """
#     """
#     len_string = len(string)
#     if len_string == 1:
#         return 0
#     # 
#     result_string = ''
#     rev_string = string[::-1]
#     # print(rev_string, ' - rev_string')
#     # 
#     pivot = 0
#     start_i = i = 1
#     while i < len_string:
#         if rev_string[i] == rev_string[pivot]:
#             # print(rev_string[i:])
#             result_string += rev_string[i]
#             if pivot == 0:
#                 start_i = i
#             pivot += 1
#         # 
#         elif pivot > 0 and rev_string[i] != rev_string[pivot] :
#             # print(rev_string[i:], rev_string[i], pivot, rev_string[pivot])
#             pivot = 0
#             result_string = ''
#             i = start_i
#         # 
#         i += 1
#     # 
#     if len(result_string) == 0 and string[0] == string[-1]:
#         return 1
#     else:
#         return len(result_string)


# # -------------------------------------------------------------------------------------------------


# def patterSearch(text, pattern):
#     """
#     """
#     len_string = len(text)
#     len_pattern = len(pattern)
#     # 
#     result_list = []
#     pivot = 0
#     start_i = i = 0
#     while i < len_string:
#         print(text[i:], pivot)
#         if pivot > 0 and text[i] != pattern[pivot] :
#             print(text[i:], text[i], pivot, text[pivot])
#             pivot = 0
#             i = start_i
#         # 
#         elif pattern[pivot] == text[i]:
#             if pivot == 0:
#                 start_i = i
#             pivot += 1
#             if pivot == len_pattern:
#                 result_list.append(start_i)
#                 pivot = 0
#                 i = start_i
#         # 
#         i += 1
#     # 
#     return result_list


# # -------------------------------------------------------------------------------------------------

# from collections import Counter

# def transformOneStringToAnother(string_1, string_2):
#     """
#     """
#     if Counter(string_1) != Counter(string_2):
#         return 'Unable to transform'
#     # 
#     res = 0
#     i = n-1
#     j = n-1    
#     while i >= 0:
#     # 
#         # if there is a mismatch, then keep incrementing
#         # result 'res' until B[j] is not found in A[0..i]
#         while i>= 0 and A[i] != B[j]:
#             i -= 1
#             res += 1
#             # 
#         # if A[i] and B[j] match
#         if i >= 0:
#             i -= 1
#             j -= 1
#             # 
#     return res


# # -------------------------------------------------------------------------------------------------


# def minWindow(self, s1, s2):
#     """
#     same as above
#     def smallest_window(s1, s2):
#     """


# # -------------------------------------------------------------------------------------------------


