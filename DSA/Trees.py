Binarytree

from binarytree import Node
root = Node(3)
root.left = Node(6)
root.right = Node(8)
  
# Getting binary tree
print('Binary tree :', root)
  
# Getting list of nodes
print('List of nodes :', list(root))
  
# Getting inorder of nodes
print('Inorder of nodes :', root.inorder)
  
# Checking tree properties
print('Size of tree :', root.size)
print('Height of tree :', root.height)
  
# Get all properties at once
print('Properties of tree : \n', root.properties)

# --------------------------------------------------------------------------------------------------

Build a binary tree from the List:
Instead of using the Node method repeatedly, we can use build() method to convert a list of values into a binary tree. 
Here, a given list contains the nodes of tree such that the element at index i has its left child at index 2*i+1, the right child at index 2*i+2 and parent at (i – 1)//2.
The elements at index j for j>len(list)//2 are leaf nodes.
None indicates the absence of a node at that index. We can also get the list of nodes back after building a binary tree using values attribute.

# Creating binary tree 
# from given list
from binarytree import build
  
  
# List of nodes
nodes =[3, 6, 8, 2, 11, None, 13]
  
# Building the binary tree
binary_tree = build(nodes)
print('Binary tree from list :\n',
      binary_tree)
  
# Getting list of nodes from
# binarytree
print('\nList from binary tree :', 
      binary_tree.values)

Output:

Binary tree from list :
 
    ___3
   /    \
  6      8
 / \      \
2   11     13


List from binary tree : [3, 6, 8, 2, 11, None, 13]

# --------------------------------------------------------------------------------------------------

from binarytree import tree
  
  
# Create a random binary 
# tree of any height
root = tree()
print("Binary tree of any height :")
print(root)
  
# Create a random binary 
# tree of given height
root2 = tree(height = 2)
print("Binary tree of given height :")
print(root2)
  
# Create a random perfect 
# binary tree of given height
root3 = tree(height = 2,
             is_perfect = True)
print("Perfect binary tree of given height :")
print(root3)
Output: 

Binary tree of any height :

      14____
     /      \
    2        5__
   /        /   \
  6        1     13
 /        /     /  \
7        9     4    8

Binary tree of given height :

  1__
 /   \
5     2
     / \
    4   3

Perfect binary tree of given height :

    __3__
   /     \
  2       4
 / \     / \
6   0   1   5