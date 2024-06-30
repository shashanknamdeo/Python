def factoral(n):
    value = 1
    for i in range(1, n+1):
        value = value*i
    return value

def factoralRecursive(n):
    if n == 1:
        return 1
    else:
        return factoralRecursive(n-1)*n

def fibonacciRecursive(n):
    if n == 0:
        return 1
    elif n== 1:
        return 1
    else:
        return fibonacciRecursive(n-1)+fibonacciRecursive(n-2)


