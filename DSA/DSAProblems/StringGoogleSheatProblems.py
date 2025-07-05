
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

from collections import Counter
from collections import defaultdict


# def smallestWindow(s1, s2):
#     """
#     """
#     s2_dict = dict(Counter(s2))
#     # 
#     length_s1 = len(s1)
#     left = 0
#     right = length_s1 - 2
#     #
#     s1_dict = dict(Counter(s1))
#     for char in s2_dict:
#         if s1_dict[char] < s2_dict[char]:
#             return ''
#     # 
#     right_fix = False
#     while right_fix == False:
#         sub_string = s1[:right]
#         sub_dict = defaultdict(int)
#         sub_dict =sub_dict | dict(Counter(sub_string))
#         for char in s2_dict:
#             print('char : ', char, 'sub_dict[char] : ', sub_dict[char], 's2_dict[char] : ', s2_dict[char])
#             if sub_dict[char] < s2_dict[char]:
#                 right += 2
#                 right_fix = True
#                 break
#         right -= 1
#     # 
#     print(right)
#     left_fix = False
#     while left_fix == False:
#         sub_string = s1[left:right]
#         sub_dict = defaultdict(int)
#         sub_dict =sub_dict | dict(Counter(sub_string))
#         for char in s2_dict:
#             print('char : ', char, 'sub_dict[char] : ', sub_dict[char], 's2_dict[char] : ', s2_dict[char])
#             if sub_dict[char] < s2_dict[char]:
#                 left -= 2
#                 left_fix = True
#                 break
#         left += 1
#     # 
#     return s1[left:right]


def smallestWindow(s1, s2):
    """
    """
    s1_dict = defaultdict(int)
    s1_dict = s1_dict | dict(Counter(s1))
    s2_dict = dict(Counter(s2))
    # 
    for char in s2_dict:
        if s1_dict[char] < s2_dict[char]:
            return ''
    #
    length_s1 = len(s1)
    min_string = s1
    min_length = length_s1
    # 
    for left in range(0, length_s1):
        # 
        for right in range(left+1, length_s1+1):
            sub_string = s1[left:right]
            print(sub_string)
            sub_dict = defaultdict(int)
            sub_dict =sub_dict | dict(Counter(sub_string))
            # 
            s2_found = True
            for char in s2_dict:
                # print('char : ', char, 'sub_dict[char] : ', sub_dict[char], 's2_dict[char] : ', s2_dict[char])
                if sub_dict[char] < s2_dict[char]:
                    # print('break')
                    s2_found = False
                    break
            # 
            if s2_found == True:
                print('s2_found - sub_string : ', sub_string)
                if right - left + 1 < min_length:
                    min_string = s1[left:right]
                    min_length  = right - left + 1
                break
    # 
    return min_string



# s1 = "zoomlazapzo"
# s2 = "oza"


s1 = "zoom"
s2 = "zooe"

print(smallestWindow(s1=s1, s2=s2))