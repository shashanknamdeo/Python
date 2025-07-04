# Set

# typecasting list to set
myset = set(["a", "b", "c"])

# Adding element to the set
myset.add("d")

# delete element from a set
myset.remove('d') #  delete a specific element from a set. If the element is not found in the set, it raises a KeyError.
myset.discard('d') # method can be used to remove an element, and it will not raise an error if the element is not present.

# -------------------------------------------------------------------------------------------------

# a set cannot have duplicate values
myset = {"Geeks", "for", "Geeks"}
print(myset) -> {'Geeks', 'for'}

 
# values of a set cannot be changed
myset[1] = "Hello"
print(myset) -> TypeError: 'set' object does not support item assignment

'''
Frozen sets in Python are immutable objects that only support methods and operators that produce a result without affecting the frozen set or sets to which they are applied.
 It can be done with frozenset() method in Python.

While elements of a set can be modified at any time, elements of the frozen set remain the same after creation. 

If no parameters are passed, it returns an empty frozenset
'''

normal_set = set(["a", "b","c"])
 
print("Normal Set")
print(normal_set)
 
# A frozen set
frozen_set = frozenset(["e", "f", "g"])
 
print("\nFrozen Set")
print(frozen_set)


# --------------------------------------------------------------------------------------------------
'''
Two sets can be merged using union() function or | operator. Both Hash Table values are accessed and traversed with merge operation perform on them to combine 
the elements, at the same time duplicates are removed. The Time Complexity of this is O(len(s1) + len(s2)) where s1 and s2 are two sets whose union needs to be done.
'''

people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
dracula = {"Deepanshu", "Raju"}
 
# Union using union()
# function
population = people.union(vampires)
 
print("Union using union() function")
print(population)
 
# Union using "|"
# operator
population = people|dracula
 
print("\nUnion using '|' operator")
print(population)

Operators        Notes

key in s         containment check
key not in s     non-containment check
s1 == s2         s1 is equivalent to s2
s1 != s2         s1 is not equivalent to s2
s1 <= s2         s1 is subset of s2
s1 < s2          s1 is proper subset of s2
s1 >= s2         s1 is superset of s2
s1 > s2          s1 is proper superset of s2
s1 | s2          the union of s1 and s2
s1 & s2          the intersection of s1 and s2
s1 – s2          the set of elements in s1 but not s2
s1 ˆ s2          the set of elements in precisely one of s1 or s2