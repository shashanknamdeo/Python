"""
Data Structures

1. Arrays
2. Strings
3. Linked Lists
    Singly Linked List
    Doubly Linked List
    Circular Linked List
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

"""

TOPIC FOR UNDERSTAND
    circular queue
    priotity queue


IMPLIMENTATION
    Singly Linked List
    Doubly Linked List
    Circular Linked List


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

# _____________________________________________________________________________________________

# STACK

push(x)             -   Add element x to the top of the stack
pop()               -   Remove the top element
top() or peek()     -   See the top element without removing it
isEmpty()           -   Check if the stack is empty
size()              -   Get the number of elements in the stack

"""
Important Stack Problems (With Concepts)

1. Valid Parentheses
    Check if the brackets are balanced.
   Example: `()[]{}` is valid, but `([)]` is not.
2. Next Greater Element
    For each element, find the next element greater than it.
   Example: For `[4, 5, 2, 10]` → Output: `[5, 10, 10, -1]`
3. Min Stack
    Design a stack that supports push, pop, and getting the minimum in constant time.
4. Largest Rectangle in Histogram
    Find the area of the largest rectangle that can be formed using bars of different heights.
5. Daily Temperatures
    For each day, tell how many days you’d have to wait for a warmer temperature.
6. Remove K Digits
    Remove `k` digits from a number string to make it the smallest possible number.
7. Asteroid Collision
    Simulate collisions between asteroids moving in opposite directions.
8. Stock Span Problem
    Find how many consecutive days before today had stock price less than or equal to today’s.
9. Implement Queue using Stacks
    Use two stacks to simulate queue behavior (FIFO).
10. Celebrity Problem
     Find the celebrity (person who is known by everyone but knows no one).

"""

# _____________________________________________________________________________________________


# QUEUE

enqueue(x)      -   Add element x to the end of the queue
dequeue()       -   Remove the element from the front
peek()          -   View the front element without removing
is_empty()      -   Check if the queue is empty
size()          -   Get the number of elements in the queue


"""
Important Queue Problems in DSA

1. Implement Queue using Stacks
    Use two stacks to implement a queue.
    Shows understanding of stack and queue logic together.
2. Implement Circular Queue
    Avoid wasting space using a circular approach.
    Very useful for fixed-size buffer problems.
3. First Non-Repeating Character in a Stream
    Given a stream of characters, find the first non-repeating character at every step.
    Uses queue + frequency map.
4. Reverse First K Elements of a Queue
    Reverse the first `k` elements of a queue using only queue operations.
    Uses queue + stack.
5. Generate Binary Numbers from 1 to N
    Given a number `N`, generate binary numbers from `1` to `N`.
    Example: N = 4 → Output: 1, 10, 11, 100
    Use a queue to build binary numbers.
6. Rotten Oranges (Multi-source BFS)
    Each orange can rot adjacent ones in 1 minute.
    Uses a queue for BFS.
    Very popular problem for practicing grid + queue + BFS.
7. Sliding Window Maximum
    Find max in each window of size `k` in an array.
    Uses deque (double-ended queue) for efficient solution.
8. Interleave the First Half of the Queue with the Second Half
    Input: `[1, 2, 3, 4, 5, 6]`
    Output: `[1, 4, 2, 5, 3, 6]`
    Requires careful use of queue and stack.
"""

