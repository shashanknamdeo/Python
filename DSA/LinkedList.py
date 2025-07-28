
# LINKED LIST

list1 = [3, 5, 8, 1]

"""
Singly Linked List    - Each node points to the next node only             
Doubly Linked List    - Each node points to both next and previous nodes
Circular Linked List  - Last node connects back to the head node          
"""

head # starting pointer of linked list


"""
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
