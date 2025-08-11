
s = "hello"

print(len(s))            # Length
print(s[1])              # Indexing
print(s[1:4])            # Slicing (ell)
print(s.upper())         # Uppercase
print(s[::_1])           # Reverse
print("e" in s)          # Search (True)

"""

strings are immutable (you can’t directly change them once created)

Why Strings Matter in DSA :
1. Used in parsing, pattern matching, encoding/decoding, etc.
2. Many problems involve substrings, palindromes, anagrams, etc.
3. Useful in hashing, dynamic programming, and sliding window problems.


Important String Problems in DSA

1. Reverse a string
2. Check for palindrome
3. Check if two strings are anagrams
4. Longest Common Substring / Subsequence (DP)
5. Longest Palindromic Substring (DP or expand_around_center)
6. String compression
7. Rabin_Karp or KMP algorithm for pattern matching
8. Z_algorithm / Prefix function (advanced pattern search)
9. Count and print all substrings
10. Sliding window problems
    Longest substring without repeating characters
    Maximum number of vowels in a substring of length `k`

"""

# Regular expresion

import re

# Function        Description
re.sub()        Replaces all occurrences of a character or patter with a replacement string.
re.split()      Split string by the occurrences of a character or a pattern.
re.escape()     Escapes special character
re.search()     Searches for first occurrence of character or pattern
re.findall()    finds and returns all matching occurrences in a list
re.compile()    Regular expressions are compiled into pattern objects


# ord() and chr()

ord() # give numeric value belong to input character (input length = 1)

ord('A') = 65

chr() # give character value belong to input numeric (input length = 1)

chr(65) = 'A'


# To remove white space in a string from front (white space - by default)
.lstrip()

"   Hello Python!".lstrip() # -> 'Hello Python!'


# To check string is a digit
.isdigit()

'10'.isdigit() # -> True

