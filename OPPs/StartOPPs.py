"""
Why 'self' use

'self' is used so that we can access variable allover in class in any methord

if we declare a variable in one function without 'self' it can't be access from another function

Important: 
    if we declare any variable in a function with 'self' it exist until instance of class exist 
    but if we declare any variable in a function without 'self' it exist only until the function is exicuting

"""

class Student:
    def __init__(self, name):
        self.name = name   # attaches 'name' to this object

    def say_hello(self):
        print("Hello, I am", self.name)

s1 = Student("Shashank")
s2 = Student("Ram")
