def generateRandomNumber(range_start, range_end, list_length):
    """
    A Function To Generate Random Numbers In A Range With A List Length
    """
    import random
    return [random.randint(range_start,range_end) for n in range(0,list_length)]




