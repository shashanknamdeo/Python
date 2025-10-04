
def isPossible(self, k, array_1, array_2):
    """
    """
    if len(array_1) != len(array_2):
        return False
    # 
    array_1.sort()
    array_2.sort()
    array_2.reverse()
    # 
    for i in range(0, len(array_1)):
        if array_1[i] + array_2[i] < k:
            return False
    # 
    return True


def countSort(string):
    """
    def countSort(self,string):
    """
    alphabet_map = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
    'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    # 
    count_array = [0] * 27
    # 
    for item in string:
        count_array[alphabet_map[item]] += 1
    # 
    for i in range(1, 27):
        count_array[i] = count_array[i] + count_array[i-1]
    # 
    print(count_array)
    answer_list = ['#'] * count_array[-1]
    # 
    for i in range(len(string)-1, -1, -1):
        char = string[i]
        char_count = count_array[alphabet_map[char]]
        print(char_count)
        answer_list[char_count - 1] = char
        count_array[alphabet_map[char]] = char_count - 1
    # 
    return "".join(answer_list)


string = "geeksforgeeks"
print(countSort(string))










































"""
https://www.geeksforgeeks.org/dsa/merge-sort-for-linked-list/
https://www.geeksforgeeks.org/dsa/quicksort-on-singly-linked-list/
"""