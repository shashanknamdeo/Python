
# def ratInMaze(maze):
#     """
#     """
#     size = len(maze)
#     response = solution(row=0, col=0, maze=maze, size=size)
#     if response[0]:
#         return response[1]
#     # 
#     return False, []


# def solution(row, col, maze, size):
#     """
#     """
#     if row == size-1 and col == size-1:
#         return True, ['']
#     # 
#     maze[row][col] = 0
#     # 
#     path_list = []
#     for direction, temp_row, temp_col in [('D', row+1, col), ('L', row, col-1), ('R', row, col+1), ('U', row-1, col)]:
#         if temp_row >= 0 and temp_row < size and temp_col >= 0 and temp_col < size and maze[temp_row][temp_col] == 1:
#             response = solution(row=temp_row, col=temp_col, maze=maze, size=size)
#             # print(row, col, direction, temp_row, temp_col, maze[temp_row][temp_col], response)
#             if response[0]:
#                 for path in response[1]:
#                     path_list.append(direction + path)
#     # 
#     maze[row][col] = 1
#     if path_list:
#         return True, path_list
#     # 
#     return False, None

# # -------------------------------------------------------------------------------------------------


def targetSumComb(array, target):
    """
    """
    array.sort()
    response = solution(array=array, target=target)
    # 
    if response[0]:
        return response[1]
    # 
    return []


def solution(array, target):
    """
    """
    if target == 0:
        print('answer found')
        return True, [[]]
    # 
    elif target < array[0]:
        return False, None
    # 
    answer_list = []
    # 
    for i in range(0, len(array)):
        response = solution(array=array[i:], target=target-array[i])
        # print(response)
        if response[0]:
            for answer in response[1]:
                print('answer:', answer)
                answer_list.append([array[i]] + answer)
    # 
    # print('answer_list:', answer_list)
    if answer_list:
        return True, answer_list
    # 
    return False, None













array = [1, 2, 3]
target = 5

array = [2, 4]
target = 1

print(targetSumComb(array=array, target=target))



































# def exist(board, word):
#     """
#     https://leetcode.com/problems/word-search/
#     """