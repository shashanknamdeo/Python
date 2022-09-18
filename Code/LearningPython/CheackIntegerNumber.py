def toCheckInteger(n):
    import math
    a = math.floor(n)
    b = n/a
    if b == 1.0:
        return "integer"
    else:
        return "non integer"