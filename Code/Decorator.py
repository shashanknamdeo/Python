"""

A decorator is a function that wraps another function and adds extra functionality.

Why use decorators?
    Keep code clean
    Reuse functionality
    Separate concerns (logging, auth, caching)
    Enhance functions without modifying them

NOTE : PYTHON APPLIES DECORATORS BOTTOM TO TOP.

"""

# insted of write

def decorator_function(original_function):
    def wrapper():
        print("Something before the function runs")
        original_function()
        print("Something after the function runs")
    return wrapper

def say_hello():
    print("Hello!")

say_hello = decorator_function(say_hello)
say_hello()

# we can write

def decorator_function(original_function):
    def wrapper():
        print("Before")
        original_function()
        print("After")
    return wrapper

@decorator_function
def say_hello():
    print("Hello!")

say_hello()     # meaning -> decorator_function(say_hello())


# -----------------------------------------------


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    return Response({"user": request.user.username})

"""

Meaning   ->  profile = api_view(['GET'])(permission_classes([IsAuthenticated])(profile))

Flow  : api_view -> permission_classes -> profile

Flow of request :
    Client Request
          ↓
    Django HttpRequest
          ↓
    api_view wrapper
      → converts to DRF (Django Rest Framework) Request
      → checks method
          ↓
    permission_classes wrapper
      → checks request.user
          ↓
    profile(request)
          ↓
    Response returned

"""

# -----------------------------------------------

"""

What are *args and **kwargs?

They allow a function to accept any number of arguments.

Syntax  Meaning
*args       collects positional arguments into a tuple
**kwargs    collects keyword arguments into a dictionary

Think of *args and **kwargs like a universal adapter 
They let your decorator fit any function, no matter its parameters.

"""

def demo(*args):
    print(args)

demo(1, 2, 3)

# Output:
(1, 2, 3)


def demo(**kwargs):
    print(kwargs)

demo(name="Aman", age=20)

# Output:
{'name': 'Aman', 'age': 20}
