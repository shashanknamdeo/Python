"""
Data Structures

1. Arrays
2. Strings
3. Linked Lists
    Singly Linked List
    Doubly Linked List
4. Stacks
5. Queues
    Circular Queue
    Priority Queue
6. Hashing
    Hash Tables
    Collision Handling (Chaining, Open Addressing)
7. Trees
    Binary Tree
    Binary Search Tree (BST)
    AVL Tree
    Segment Tree / Fenwick Tree
    Trie
8. Graphs
    Representations (Adjacency Matrix/List)
    BFS, DFS
    Topological Sorting
    Shortest Path (Dijkstra, Bellman_Ford, Floyd_Warshall)
    Minimum Spanning Tree (Prim’s, Kruskal’s)
9. Heaps
    Min_Heap / Max_Heap
    Heap Sort



Algorithms

1. Sorting
    Bubble, Selection, Insertion
    Merge Sort
    Quick Sort
    Counting / Radix Sort

2. Searching
    Linear Search
    Binary Search (on arrays, answer_based)

3. Recursion & Backtracking
    N_Queens, Sudoku Solver
    Subset/Permutation Generation

4. Dynamic Programming
    Memoization & Tabulation
    Knapsack Problems
    Longest Common Subsequence (LCS), LIS
    Matrix Chain Multiplication

5. Greedy Algorithms
    Activity Selection
    Huffman Coding

6. Divide and Conquer
    Merge Sort
    Binary Search

7. Bit Manipulation
    XOR problems
    Power of 2

8. Sliding Window
    Maximum sum subarray

9. Two Pointer Technique

10. Union_Find / Disjoint Set
"""

# _____________________________________________________________________________________________
"""
IMPORTANT TOPIC RELATED TO DSA

1. Hash value :
    A hash value in Python is an integer that uniquely represents an object.
    It's obtained using the built-in hash() function. 
    Hash values are primarily used for quick comparisons of dictionary keys during lookups. 
    They play a crucial role in the efficient operation of dictionaries and sets. 
    Only immutable objects like numbers, strings, and tuples can be hashed. 
    Attempting to hash a mutable object, such as a list or a dictionary, will result in a TypeError.

"""

# _____________________________________________________________________________________________

# ARRAY

# methord 1
import array
array.array('i', [1, 2, 3, 4])

# methord 2
import numpy as np
# 1D array
arr = np.array([10, 20, 30, 40])
# 2D array
matrix = np.array([[1, 2], [3, 4]])

# Note : numpy array is best

# _____________________________________________________________________________________________

# LINKED LIST

"""
Singly Linked List    - Each node points to the next node only             
Doubly Linked List    - Each node points to both next and previous nodes
Circular Linked List  - Last node connects back to the head node          


Common Linked List Problems in DSA

1. Reverse a Linked List
2. Detect Loop (Cycle Detection using Floyd’s Algorithm)
3. Find the Middle of the List
4. Merge Two Sorted Linked Lists
5. Delete a Node
6. Find Intersection Point of Two Lists
7. Check if a Linked List is a Palindrome
8. Remove N_th node from end
9. Clone a Linked List with Random Pointers
10. Add Two Numbers Represented by Linked Lists


Advantages
1. Dynamic size
2. Efficient insertion/deletion (no shifting like arrays)

Disadvantages
1. No random access (unlike arrays)
2. Extra memory for pointers


Feature                      | Array                              | Linked List                            
_____________________________|____________________________________|_________________________________________
Memory Allocation            | Contiguous (fixed size or dynamic) | Non_contiguous (each node has a pointer)
Access (Random Access)       | Fast (O(1))                        | Slow (O(n), sequential traversal)      
Insertion (at end)           | Fast (if space available, O(1))    | Fast (O(1) with tail pointer)          
Insertion (in middle/start)  | Slow (O(n), needs shifting)        | Fast (O(1) for start, O(n) for middle)
Deletion (from middle/start) | Slow (O(n))                        | Fast (O(1) for start, O(n) for middle)
Memory Usage                 | Less (just data)                   | More (data + pointer in each node)      
Resizing                     | Costly (copying needed)            | Easy (just add nodes)                   
Cache Friendliness           | High                               | Low (nodes spread in memory)           
Implementation Simplicity    | Simple                             | More complex (pointer management)      

"""

# _____________________________________________________________________________________________

# STRING

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

