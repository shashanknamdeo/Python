# Accessing Dictionary Items

dictionary["key"]

dictionary.get(key[, default_value])

# The dict.get() method in Python retrieves the value associated with a specified key from 
# a dictionary. It offers a safer alternative to direct key access using square brackets (dict[key]) 
# because it handles cases where the key might not exist in the dictionary.

# If the key is present in the dictionary, the method returns the value associated with that key.
# If the key is not found and default_value is provided, default_value is returned.
# If the key is not found and default_value is not provided, None is returned.

ex :

d.get("salary", 0)



# Removing Dictionary Items

del         : Removes an item by key.
pop()       : Removes an item by key and returns its value.
clear()     : Empties the dictionary.
popitem()   : Removes and returns the last key-value pair.

# ex :

del d["age"]

# Using pop() to remove an item and return the value
val = d.pop(1)

# Using popitem to removes and returns
# the last key-value pair.
key, val = d.popitem()

# Clear all items from the dictionary
d.clear()



# Defaultdict in Python

# It is used to provide a default value for a nonexistent key in the dictionary

from collections import defaultdict

# Using int: If you use int as the factory function, the default value will be 0 (since int() returns 0).
d = defaultdict(int)

# Using list: If you use list as the factory function, the default value will be an empty list ([]).
d = defaultdict(list)

# Using str: If you use str, the default value will be an empty string ('').
d = defaultdict(str)

# Defining the dict and passing lambda as default_factory argument
d = defaultdict(lambda: "Not Present")




