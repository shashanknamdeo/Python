
# Array

def prefixSum(array):
    """
    """
    prefix = [0] * len(array)
    prefix[0] = array[0]
    for i in range(1, len(array)):
        prefix[i] = prefix[i - 1] + array[i]
    return prefix


# -------------------------------------------------------------------------------------------------


def rangeSum(array, L, R):
    """
    sum of item from array[L] to array[R]
    item array[L] and array[R] are included in sum
    """
    prefix = build_prefix_sum(array=array)
    if L == 0:
        return prefix[R]
    else:
        return prefix[R] - prefix[L - 1]


# -------------------------------------------------------------------------------------------------


def findPivotElementIndex(array):
    """
    To find the pivort element index in sorted then roted array
    ex - array = [4, 5, 6, 7, 0, 1, 2]
    return 4
    """
    left, right = 0, len(array) - 1
    # 
    # If arrayay is not rotated
    if array[left] <= array[right]:
        return 0
    # 
    while left <= right:
        mid = (left + right) // 2
        # 
        # Check if mid is pivot
        if array[mid] > array[mid + 1]:
            return mid + 1
        if array[mid - 1] > array[mid]:
            return mid
        # 
        # Decide which half to search
        if array[mid] >= array[left]:
            left = mid + 1
        else:
            right = mid - 1
    # 
    return 0  # fallback
