[ x for j in range(0, 10) for x in range(0,10)]
[ x+j for j in range(0, 10) for x in range(0,10)]
[ x+j for j in range(0, 10) for x in range(0,10)]
->list = [i for i in range(11) if i % 2 == 0]
  print(list)
->matrix = [[j for j in range(3)] for i in range(3)]

List Methods
Function  Description
Append()  Add an element to the end of the list
Extend()  Add all elements of a list to another list
Insert()  Insert an item at the defined index
Remove()  Removes an item from the list
Clear() Removes all items from the list
Index() Returns the index of the first matched item
Count() Returns the count of the number of items passed as an argument
Sort()  Sort items in a list in ascending order
Reverse() Reverse the order of items in the list
copy()  Returns a copy of the list

Built-in functions with List
Function  Description
reduce()  apply a particular function passed in its argument to all of the list elements stores the intermediate result and only returns the final summation value
sum() Sums up the numbers in the list
ord() Returns an integer representing the Unicode code point of the given Unicode character
cmp() This function returns 1 if the first list is “greater” than the second list
max() return maximum element of a given list
min() return minimum element of a given lists
all() Returns true if all element is true or if the list is empty
any() return true if any element of the list is true. if the list is empty, return false
len() Returns length of the list or size of the list
enumerate() Returns enumerate object of the list
accumulate()  apply a particular function passed in its argument to all of the list elements returns a list containing the intermediate results
filter()  tests if each element of a list is true or not
map() returns a list of the results after applying the given function to each item of a given iterable
lambda()  This function can have any number of arguments but only one expression, which is evaluated and returned.
----------------------------------------------------------------------------
dictionary:-

ex1:- dict = {1:'A',2:'B',3:'C'}
      dict[1] -> 'A'
ex2:- dict = {'Name' : 'Shashank Namdeo' , 'Class' : '12' , 'Section' : 'A' , 'School' : 'Modal H. S. School' , 'Address' : 'Bhopal' }


clear() – Remove all the elements from the dictionary
copy() – Returns a copy of the dictionary
get() – Returns the value of specified key
items() – Returns a list containing a tuple for each key value pair
keys() – Returns a list containing dictionary’s keys
pop() – Remove the element with specified key
popitem() – Removes the last inserted key-value pair
update() – Updates dictionary with specified key-value pairs
values() – Returns a list of all the values of dictionary