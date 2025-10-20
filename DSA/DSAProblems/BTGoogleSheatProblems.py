
import copy

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


# def targetSumComb(array, target):
#     """
#     """
#     array.sort()
#     response = solution(array=array, target=target)
#     # 
#     if response[0]:
#         return response[1]
#     # 
#     return []


# def solution(array, target):
#     """
#     """
#     if target == 0:
#         print('answer found')
#         return True, [[]]
#     # 
#     elif target < array[0]:
#         return False, None
#     # 
#     answer_list = []
#     # 
#     for i in range(0, len(array)):
#         response = solution(array=array[i:], target=target-array[i])
#         # print(response)
#         if response[0]:
#             for answer in response[1]:
#                 print('answer:', answer)
#                 answer_list.append([array[i]] + answer)
#     # 
#     # print('answer_list:', answer_list)
#     if answer_list:
#         return True, answer_list
#     # 
#     return False, None


# # -------------------------------------------------------------------------------------------------


# def findBlankRecursively(row, col, matrix, size):
#     """
#     """
#     print('int - findBlank : ', row, col)
#     vertical = False
#     if (row-1 >= 0 and matrix[row-1][col] == '-') or (row+1 < size and matrix[row+1][col] == '-'):
#         vertical = True
#     # 
#     temp_row = row
#     temp_col = col
#     blank_length = 0
#     blank_block_list = []
#     new_blank = []
#     # 
#     if vertical:
#         while temp_row-1 >= 0 and  matrix[temp_row-1][temp_col] == '-':
#             temp_row -= 1
#         # 
#         col_prev = False
#         col_next = False
#         if col-1 >= 0:
#             col_prev = True
#         if col+1 < size:
#             col_next = True
#         # 
#         blank_block = []
#         while temp_row < size and matrix[temp_row][temp_col] == '-':
#             blank_block.append((temp_row, temp_col))
#             matrix[temp_row][temp_col] = '#'
#             # 
#             if (col_prev and matrix[temp_row][temp_col-1] == '-') or (col_next and matrix[temp_row][temp_col+1] == '-'):
#                 matrix[temp_row][temp_col] = '-'
#                 new_blank.append((temp_row, temp_col))
#             # 
#             temp_row += 1
#             blank_length += 1
#         # 
#         blank_block_list.append(blank_block)
#     # 
#     if not vertical:
#         while temp_col-1 >= 0 and  matrix[temp_row][temp_col-1] == '-':
#             temp_col -= 1
#         # 
#         row_prev = False
#         row_next = False
#         if row-1 >= 0:
#             row_prev = True
#         if row+1 < size:
#             row_next = True
#         # 
#         blank_block = []
#         while temp_col < size and matrix[temp_row][temp_col] == '-':
#             blank_block.append((temp_row, temp_col))
#             matrix[temp_row][temp_col] = '#'
#             # 
#             if (row_prev and matrix[temp_row-1][temp_col] == '-') or (row_next and matrix[temp_row+1][temp_col] == '-'):
#                 matrix[temp_row][temp_col] = '-'
#                 new_blank.append((temp_row, temp_col))
#             # 
#             temp_col += 1
#             blank_length += 1
#         # 
#         blank_block_list.append(blank_block)
#     # 
#     if new_blank:
#         for item in new_blank:
#             response = findBlankRecursively(row=item[0], col=item[1], matrix=matrix, size=size)
#             blank_block_list += response
#     # 
#     print(row, col, blank_block_list)
#     return blank_block_list


# def findBlank(matrix, words, size):
#     """
#     """
#     size = len(matrix)
#     blank_block_list = []
#     # 
#     for i in range(0, size):
#         for j in range(0, size):
#             if matrix[i][j] == '-':
#                 blank_block_list += findBlankRecursively(row=i, col=j, matrix=matrix, size=size)
#     # 
#     return blank_block_list


# def crosswordPuzzle(matrix, words):
#     """
#     """
#     size = len(matrix)
#     words = words.split(';')
#     # 
#     for i in range(0, size):
#         matrix[i] = list(matrix[i])
#     # 
#     blank_block_list = findBlank(matrix=matrix, words=words, size=size)
#     print(blank_block_list)
#     while [] in blank_block_list:
#         blank_block_list.pop(blank_block_list.index([]))
#     # 
#     length = len(blank_block_list)
#     response = fillWordInBlank(matrix=matrix, blank_block_list=blank_block_list, words=words, length=length)
#     print(response[0])
#     matrix = response[1]
#     # 
#     for i in range(0, size):
#         matrix[i] = "".join(matrix[i])
#     # 
#     return matrix


# def fillWordInBlank(matrix, blank_block_list, words, length):
#     """
#     """
#     print('\ninit - fillWordInBlank : ', length, words)
#     if length == 0:
#         return True, matrix
#     # 
#     matrix_copy = copy.deepcopy(matrix)
#     blank_block = blank_block_list[-1]
#     len_blank = len(blank_block)
#     for i in range(0, length):
#         print(i, words[i], len_blank)
#         if len(words[i]) == len_blank:
#             # print(matrix)
#             response_1 = fillLatterInBlock(matrix=matrix_copy, blank_block=blank_block, word=words[i])
#             print('response_1 :', response_1[0], length)
#             if response_1[0]:
#                 new_words = copy.deepcopy(words)
#                 new_words.pop(i)
#                 response_2 = fillWordInBlank(matrix=response_1[1], blank_block_list=blank_block_list[:-1], words=new_words, length=length-1)
#                 print('response_2 :', response_2[0], length)
#                 if response_2[0]:
#                     return True, response_2[1]
#         # 
#         matrix_copy = copy.deepcopy(matrix)
#         # print('matrix_copy : ', matrix_copy)
#     # 
#     return False, None


# def fillLatterInBlock(matrix, blank_block, word):
#     """
#     """
#     print('\ninit - fillWordInBlock : ', blank_block, word)
#     temp_matrix = copy.deepcopy(matrix)
#     # 
#     index = 0
#     for row, col in blank_block:
#         if temp_matrix[row][col] == '#':
#             temp_matrix[row][col] = word[index]
#         # 
#         elif temp_matrix[row][col] != word[index]:
#             print('fillLatterInBlock - False \n \n temp_matrix[row][col] :', temp_matrix[row][col], '\n word[index] : ', word[index], '\n')
#             return False, matrix
#         # 
#         index += 1
#     # 
#     # print(matrix)
#     # exit()
#     return True, temp_matrix


# # -------------------------------------------------------------------------------------------------


# def longestPath(self, matrix, m, n, xs, ys, xd, yd):
#         """
#         """
#         if matrix[xs][ys] == 0 or matrix[xd][yd] == 0:
#             return -1
#         # 
#         response = longestPathRecursively(matrix=matrix, m=m, n=n, xs=xs, ys=ys, xd=xd, yd=yd)
#         # 
#         # print(response[0], response[1]-1)
#         return response[1]-1 


# def longestPathRecursively(matrix, m, n, xs, ys, xd, yd):
#     """
#     """
#     if xs == xd and ys == yd:
#         return True, 1
#     # 
#     longest_path = 0
#     matrix[xs][ys] = 2
#     adjacent_block = [(xs-1, ys), (xs+1, ys), (xs, ys-1), (xs, ys+1)]
#     for x, y in adjacent_block:
#         if x >= 0 and x < m and y >= 0 and y < n and matrix[x][y] == 1:
#             response = longestPathRecursively(matrix=matrix, m=m, n=n, xs=x, ys=y, xd=xd, yd=yd)
#             if response[0]:
#                 longest_path = max(longest_path, response[1])
#     # 
#     matrix[xs][ys] = 1
#     # 
#     if longest_path > 0:
#         return True, longest_path + 1
#     # 
#     return False, None


# # -------------------------------------------------------------------------------------------------


# def nQueen(n):
#     """
#     """
#     answer_list = []
#     answer = []
#     # 
#     row = [False]*(n+1)
#     diaginal_tl_br = [False]*(2*n+1)
#     diaginal_tr_bl = [False]*(2*n+1)
#     # 
#     nQueenRecursively(1, n, row, diaginal_tl_br, diaginal_tr_bl, answer, answer_list)
#     # 
#     return answer_list


# def nQueenRecursively(queen, n, row, diaginal_tl_br, diaginal_tr_bl, answer, answer_list):
#     """
#     """
#     # print(queen)
#     if queen > n:
#         answer_list.append(answer[:])
#         # print('answer_list : ', answer_list)
#         return
#     # 
#     for col in range(1, n+1):
#         # print('queen : ', queen, 'col : ', col)
#         if col not in answer and not row[queen] and not diaginal_tl_br[queen + col] and not diaginal_tr_bl[queen-col+n]:
#             row[queen] = diaginal_tl_br[queen + col] = diaginal_tr_bl[queen-col+n] = True
#             # print(col, row[queen], diaginal_tl_br[queen + col], diaginal_tr_bl[queen-col+n])
#             answer.append(col)
#             # print(answer)
#             nQueenRecursively(queen+1, n, row, diaginal_tl_br, diaginal_tr_bl, answer, answer_list)
#             row[queen] = diaginal_tl_br[queen + col] = diaginal_tr_bl[queen-col+n] = False
#             answer.pop()
#     # 
#     return


# # -------------------------------------------------------------------------------------------------


def getBlockArray(row, col, matrix):
    """
    """
    l = (row, col)
    block_range = [None, None]
    for i in [0,1]:
        if l[i] <= 2:
            block_range[i] = (0,3)
        elif l[i] > 5:
            block_range[i] = (6,9)
        else:
            block_range[i] = (3,6)
    # 
    block_array = []
    for i in range(block_range[0][0], block_range[0][1]):
        for j in range(block_range[1][0], block_range[1][1]):
            block_array.append(matrix[i][j])
    # 
    return block_array


def getNotArray(row, col, matrix):
    """
    """
    array = [9,8,7,6,5,4,3,2,1]
    # 
    row_array = matrix[row]
    # print(row_array)
    col_array = [matrix[i][col] for i in range(0,9)]
    # print(col_array)
    block_array = getBlockArray(row=row, col=col, matrix=matrix)
    # print(block_array)
    # 
    not_array = []
    rsb_set = set(row_array + col_array + block_array)
    # 
    for item in array:
        if item not in rsb_set:
            not_array.append(item)
    # 
    return not_array


def solveSudokuRecursively(start_row, matrix):
    """
    """
    # sleep(1)
    for row in range(start_row, 9):
        for col in range(0, 9):
            if matrix[row][col] == 0:
                not_array = getNotArray(row=row, col=col, matrix=matrix)
                if not not_array:
                    # print(row, col, 'wrong ')
                    return False
                # 
                for item in not_array:
                    matrix[row][col] = item
                    # print(row, col, 'r : ', item)
                    if solveSudokuRecursively(start_row=row, matrix=matrix):
                        return True
                    matrix[row][col] = 0
                # 
                return False
    # 
    # print('matrix complete')
    return True


def solveSudoku(matrix):
    """
    """
    if solveSudokuRecursively(start_row=0, matrix=matrix):
        return matrix


# # -------------------------------------------------------------------------------------------------


def equalPartition(array):
    """
    """
    response = equalPartitionRecursively(a=0, b=0, array=array)
    return response[0]

import copy

def equalPartitionRecursively(a, b, array):
    """
    """
    if not array and a == b:
        return True, [], []
    # 
    elif not array and a != b:
        # print(a, b, array)
        return False, None, None
    # 
    def search(var, array):
        for i in range(0, len(array)):
            # new_array = copy.deepcopy(array)
            item = array.pop(i)
            if var == 1:
                response = equalPartitionRecursively(a=a+item, b=b, array=new_array)
            # 
            if var == 2:
                response = equalPartitionRecursively(a=a, b=b+item, array=new_array)
            # 
            # print(response, var)
            if response[0]:
                response[var].append(item)
                return response
            # 
        return False, None, None
    # 
    if a <= b:
        return search(var=1, array=array)
    # 
    else:
        return search(var=2, array=array)


array = [1, 3, 5]   

print(equalPartitionRecursively(a=0, b=0, array=array))





