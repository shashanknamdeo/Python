

def implementTwoStacksinOneArray():
    """
    n = given length of array
    unable to use OPPs concept to implement
    https://www.geeksforgeeks.org/dsa/implement-two-stacks-in-an-array/
    """
    array = [None]*n
    pointer_1 = -1
    pointer_1 = len(array)
    def push1(value):
        """
        """
        if pointer_1 + 1 < pointer_2:
            array[pointer_1] = value
            pointer_1 += 1
        else:
            print("Stack-1-is-full")
    # 
    # 
    def push2(value):
        """
        """
        if pointer_2 - 1 > pointer_1:
            array[pointer_1] = value
            pointer_1 -= 1
        else:
            print("Stack-2-is-full")
    # 
    # 
    def pop1():
        """
        """
        if pointer_1 > -1:
            pointer_1 -= 1
            return interval_array[pointer_1 + 1]
        else:
            print("Stack-1-is-empty")
            return -1
    # 
    # 
    def pop2():
        """
        """
        if pointer_1 < len(array):
            pointer_1 += 1
            return interval_array[pointer_1 - 1]
        else:
            print("Stack-2-is-empty")
            return -1












