
# https://www.geeksforgeeks.org/dsa/maximum-and-minimum-in-an-array/

def maximumAndMinimumOfArray(array):
    """
    Maximum and minimum of an array using minimum number of comparisons
    # 
    comparision = 2n - 2
    """
    current_min = array[0]
    current_max = array[0]
    # 
    for element in array :
        if element < current_min:
            current_min = element
        elif element > current_max:
            current_max = element
    # 
    return current_min, current_max


def maximumAndMinimumOfArray(array):
    """
    comparision = 1.5n - 2
    # 
    1st comparison → in the while loop condition → but it's just checking loop index, not a data comparison → ❌ not counted
    2nd comparison → if arr[i] > arr[i+1] → ✅ counted (pairwise)
    3rd comparison → max(...) → ✅ counted
    4th comparison → min(...) → ✅ counted
    """
    n = len(array)
    # 
    if n % 2 == 0:
        if array[0] > array[1]:
            current_min = array[1]
            current_max = array[0]
        else:
            current_min = array[0]
            current_max = array[1]
        # 
        i = 2
    else:
        current_min = current_max = array[0]
        i = 1
    # 
    while i < n-1:
        if array[i] > array[i+1]:
            current_min = min(current_min, array[i+1])
            current_max = max(current_max, array[i])
        # 
        else:
            current_min = min(current_min, array[i])
            current_max = max(current_max, array[i+1])
        # 
        i += 2
        print(current_min, current_max)
    # 
    return current_min, current_max


# -------------------------------------------------------------------------------------------------


# https://www.geeksforgeeks.org/dsa/program-to-reverse-an-array/

def arrayReverse(array):
    """
    Using a temporary array - O(n) Time and O(n) Space
    """
    n = len(array)-1
    temp_array = []
    # 
    while n > -1:
        temp_array.append(array[n])
        n -= 1
    # 
    return temp_array


def arrayReverse(array):
    """
    By Swapping Elements - O(n) Time and O(1) Space
    this program is correct but it has many steps
    """
    def evenArrayReverse(array, length):
        """
        """
        temp = None
        inital_index = 0
        final_index = length-1
        # 
        for i in range(0, int(length/2)):
            temp = array[i]
            array[inital_index] = array[final_index]
            array[final_index] = temp
            # 
            inital_index += 1
            final_index -= 1
        # 
        return array
    # 
    def oddArrayReverse(array, length):
        """
        """
        temp = None
        inital_index = 0
        final_index = length-1
        # 
        for i in range(0, int(length/2)):
            temp = array[i]
            array[inital_index] = array[final_index]
            array[final_index] = temp
            # 
            inital_index += 1
            final_index -= 1
        # 
        return array
    # 
    n = len(array)
    if n % 2:
        return evenArrayReverse(array=array, length=n)
    else:
        return oddArrayReverse(array=array, length=n)

