import time
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


def longestPath(self, matrix, m, n, xs, ys, xd, yd):
        """
        """
        if matrix[xs][ys] == 0 or matrix[xd][yd] == 0:
            return -1
        # 
        response = longestPathRecursively(matrix=matrix, m=m, n=n, xs=xs, ys=ys, xd=xd, yd=yd)
        # 
        # print(response[0], response[1]-1)
        return response[1]-1 


def longestPathRecursively(matrix, m, n, xs, ys, xd, yd):
    """
    """
    if xs == xd and ys == yd:
        return True, 1
    # 
    longest_path = 0
    matrix[xs][ys] = 2
    adjacent_block = [(xs-1, ys), (xs+1, ys), (xs, ys-1), (xs, ys+1)]
    for x, y in adjacent_block:
        if x >= 0 and x < m and y >= 0 and y < n and matrix[x][y] == 1:
            response = longestPathRecursively(matrix=matrix, m=m, n=n, xs=x, ys=y, xd=xd, yd=yd)
            if response[0]:
                longest_path = max(longest_path, response[1])
    # 
    matrix[xs][ys] = 1
    # 
    if longest_path > 0:
        return True, longest_path + 1
    # 
    return False, None


# # -------------------------------------------------------------------------------------------------


# def markQueenPath(row, col, matrix, size):
#     """
#     """
#     new_matrix = copy.deepcopy(matrix)
#     # check row
#     for i in range(0, size):
#         new_matrix[i][col] = 1
#     # 
#     # check col
#     for j in range(0, size):
#         new_matrix[row][j] = 1
#     # 
#     # check diagnol
#     temp_row = copy.deepcopy(row)
#     temp_col = copy.deepcopy(col)
#     while temp_row >= 0 and temp_col >= 0:
#         new_matrix[temp_row][temp_col] = 1
#         temp_row, temp_col = temp_row-1, temp_col-1
#     # 
#     temp_row = copy.deepcopy(row)
#     temp_col = copy.deepcopy(col)
#     while temp_row < size and temp_col < size:
#         new_matrix[temp_row][temp_col] = 1
#         temp_row, temp_col = temp_row+1, temp_col+1
#     # 
#     temp_row = copy.deepcopy(row)
#     temp_col = copy.deepcopy(col)
#     while temp_row >= 0 and temp_col < size:
#         new_matrix[temp_row][temp_col] = 1
#         temp_row, temp_col = temp_row-1, temp_col+1
#     # 
#     temp_row = copy.deepcopy(row)
#     temp_col = copy.deepcopy(col)
#     while temp_row < size and temp_col >= 0:
#         new_matrix[temp_row][temp_col] = 1
#         temp_row, temp_col = temp_row+1, temp_col-1
#     # 
#     return new_matrix


# def nQueen(size):
#     """
#     """
#     matrix = []
#     for i in range(0, size):
#         matrix.append([0 for _ in range(0, size)])
#     # 
#     response = findQueenPosition(matrix=matrix, size=size, queen=size)
#     if response[0]:
#         return response
#     else:
#         return []

# def findQueenPosition(matrix, size, queen):
#     """
#     """
#     if queen == 0:
#         answer_matrix = []
#         for i in range(0, size):
#             answer_matrix.append([0 for _ in range(0, size)])
#         return True, answer_matrix
#     # 
#     # 
#     new_matrix = copy.deepcopy(matrix)
#     # 
#     for i in range(0, size):
#         for j in range(0, size):
#             if new_matrix[i][j] == 0:
#                 filled_matrix = markQueenPath(row=i, col=j, matrix=new_matrix, size=size)
#                 # print(queen-1, filled_matrix)
#                 # 
#                 response = findQueenPosition(matrix=filled_matrix, size=size, queen=queen-1)
#                 if response[0]:
#                     answer_matrix = response[1]
#                     answer_matrix[i][j] = 1
#                     return True, answer_matrix
#     # 
#     return False, None


def nQueen(n):
    """
    """
    answer_list = []
    answer = []
    # 
    row = [False]*(n+1)
    diaginal_tl_br = [False]*(2*n+1)
    diaginal_tr_bl = [False]*(2*n+1)
    # 
    nQueenRecursively(1, n, row, diaginal_tl_br, diaginal_tr_bl, answer, answer_list)
    # 
    return answer_list


def nQueenRecursively(queen, n, row, diaginal_tl_br, diaginal_tr_bl, answer, answer_list):
    """
    """
    print(queen)
    if queen > n:
        answer_list.append(answer)
    # 
    for col in range(1, n+1):
        if not row[queen] and not diaginal_tl_br[queen + col] and not diaginal_tr_bl[queen-col+n]:
            row[queen] = diaginal_tl_br[queen + col] = diaginal_tr_bl[queen-col+n] = True
            answer.append(col)
            nQueenRecursively(queen+1, n, row, diaginal_tl_br, diaginal_tr_bl, answer, answer_list)
            answer.pop()




# matrix = [
# [1, 0, 1, 0], 
# [0, 1, 1, 0], 
# [1, 1, 1, 1]
# ] 

# n=4
# m=3
# xs=1
# ys=1
# xd=2
# yd=3



# print(nQueen(size=4))









a
























# def exist(board, word):
#     """
#     https://leetcode.com/problems/word-search/
#     """
