"""
functions:

'd' Signed integer decimal.  
'i' Signed integer decimal.  
'o' Signed octal value. (1)
'u' Obsolete type – it is identical to 'd'. (7)
'x' Signed hexadecimal (lowercase). (2)
'X' Signed hexadecimal (uppercase). (2)
'e' Floating point exponential format (lowercase).  (3)
'E' Floating point exponential format (uppercase).  (3)
'f' Floating point decimal format.  (3)
'F' Floating point decimal format.  (3)
'g' Floating point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.  (4)
'G' Floating point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.  (4)
'c' Single character (accepts integer or single character string).   
'r' String (converts any Python object using repr()).   (5)
's' String (converts any Python object using str()).    (6)
'%' No argument is converted, results in a '%' character in the result.
"""

# example:

print('%(language)s has %(number)03d quote types.' % {"language": "Python", "number": 2})
Python has 002 quote types.

print("My name is %s"%'Anshuman')
My name is Anshuman

print('I am %d years old'%14)
I am 14 years old

print('I am %f years old' % 14.1)
I am 14.1 years old

a = 10 % 3
print("The remainder is %d"%a)