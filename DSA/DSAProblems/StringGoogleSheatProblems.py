
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


def printSequence(arr, input):
    """
    str = ["2", "22", "222",
        "3", "33", "333",
        "4", "44", "444",
        "5", "55", "555",
        "6", "66", "666",
        "7", "77", "777", "7777",
        "8", "88", "888",
        "9", "99", "999", "9999"]
    1. make dict having A-Z having str values
    2. iterate over input and get numeric value from dict and append it to output string
    """












arr = ["flower","flow","flight"]

print(longestCommonPrefix(array=arr))