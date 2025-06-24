
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