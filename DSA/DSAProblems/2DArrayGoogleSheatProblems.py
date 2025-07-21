
# https://docs.google.com/spreadsheets/d/1hXserPuxVoWMG9Hs7y8wVdRCJTcj3xMBAEYUOXQ5Xag/edit?gid=0#gid=0

# def diagonalTraversal(matrix):
#     """
#     """
#     col = len(matrix[0])
#     row = len(matrix)
#     print('col : ', col)
#     diagonal_item = []
#     for i in range(0,col+1):
#         j = 0
#         # Follow each diagonal going up and right
#         while i >= 0 and j < col:
#             diagonal_item.append(matrix[i][j])
#             i -= 1
#             j += 1
#     #
#     # print('--------------------')
#     start_col = 1
#     while start_col < col:
#         i = row - 1
#         for j in range(start_col,col):
#             diagonal_item.append(matrix[i][j])
#             i -= 1
#         start_col += 1
#     # 
#     return diagonal_item 


# def setZeroes(matrix):
#     """
#     """
#     total_row = len(matrix)
#     total_col = len(matrix[0])
#     # 
#     zero_row = []
#     zero_col = []
#     # 
#     for i in range(0, total_row):
#         if 0 not in matrix[i]:
#             continue
#         # 
#         zero_row.append(i)
#         j = 0
#         while j < total_col:
#             if matrix[i][j] == 0:
#                 zero_col.append(j)
#             j += 1
#     # 
#     for i in zero_row:
#         matrix[i] = [0]*total_col
#     # 
#     for j in zero_col:
#         for i in range(0, total_row):
#             matrix[i][j] = 0
#     # 
#     return matrix


# def spiralOrder(matrix):
#         """
#         """
#         total_row = len(matrix)
#         total_col = len(matrix[0])
#         # 
#         traverse_list = []
#         # 
#         row_no = 0
#         col_no = 0
#         while (row_no < total_row//2 ) and (col_no < total_col//2):
#             traverse_list += spiralTraverse(matrix=matrix, row_no=row_no, col_no=col_no, total_row=total_row, total_col=total_col)
#             row_no += 1
#             col_no += 1
#         # 
#         if total_row % 2 + total_col % 2 == 1:
#             if total_row % 2 == 1:
#                 for i in range(col_no, total_col - col_no):
#                     # print(1, 'row', i)
#                     traverse_list.append(matrix[row_no][i])
#             # 
#             elif total_col % 2 == 1:
#                 for j in range(row_no, total_row - row_no):
#                     # print(1, 'col', j)
#                     traverse_list.append(matrix[j][col_no])
#         # 
#         if total_row % 2 + total_col % 2 == 2:
#             # print(2)
#             if total_row <= total_col:
#                 for i in range(col_no, total_col - col_no):
#                     traverse_list.append(matrix[row_no][i])
#             # 
#             else:
#                 for j in range(row_no, total_row - row_no):
#                     traverse_list.append(matrix[j][col_no])
#         # 
#         return traverse_list


# def spiralTraverse(matrix, row_no, col_no, total_row, total_col):
#     """
#     """
#     current_row = row_no
#     current_col = col_no
#     traverse_list = []
#     # 
#     traverse_list += matrix[current_row][current_col:total_col - current_col]
#     current_col = total_col - current_col - 1
#     # 
#     j = current_row + 1
#     while j < total_row - current_row:
#         traverse_list.append(matrix[j][current_col])
#         j += 1
#     current_row = j - 1
#     # 
#     temp_array = matrix[current_row][col_no:current_col]
#     temp_array.reverse()
#     traverse_list += temp_array
#     # 
#     j = current_row - 1
#     while j > row_no:
#         traverse_list.append(matrix[j][col_no])
#         j -= 1
#     # 
#     return traverse_list



# def rotate(matrix):
#     """
#     make 4 array
#     # 
#     another Approach:
#     step 1. Transpose the matrix (swap rows with columns).
#     step 2. Reverse each row.
#     """
#     top = left = 0
#     bottom = right = len(matrix) - 1
#     # 
#     while top < bottom:
#         ht_array = matrix[top]
#         hb_array = matrix[bottom]
#         # print(ht_array, hb_array)
#         # 
#         vl_array = []
#         vr_array = []
#         for i in range(top, bottom+1):
#             # 
#             vl_array.append(matrix[i][left])
#             matrix[i][left] = hb_array[i]
#             # 
#             vr_array.append(matrix[i][right])
#             matrix[i][right] = ht_array[i]
#             print(vl_array, vr_array)
#         # 
#         vl_array.reverse()
#         vr_array.reverse()
#         matrix[top][left:right+1] = vl_array
#         matrix[bottom][left:right+1] = vr_array
#         # 
#         top = left = top + 1
#         bottom = right = bottom - 1
#     # 
#     return matrix


# def exist(board, word):
#     """
#     https://leetcode.com/problems/word-search/
#     solve by advance topic like DP and back tracking
#     """


# def numberOfIslands():
#     """
#     https://www.geeksforgeeks.org/dsa/find-the-number-of-islands-using-dfs/
#     solve by advance topic like DFS
#     """


# def replaceOWithX():
#     """
#     https://www.geeksforgeeks.org/dsa/given-matrix-o-x-replace-o-x-surrounded-x/
#     """


# def findCommonElement(matrix):
#     """
#     my idea - implemanted by ChatGPT
#     time complexity - O(n*m)
#     """
#     m = len(matrix)
#     n = len(matrix[0])
#     # 
#     # Initialize a pointer for each row (start from column 0)
#     indices = [0] * m
#     # 
#     # Initialize max_num as the first element of the first row
#     max_num = matrix[0][0]
#     # 
#     while True:
#         count_equal = 0  # Counts how many rows are currently at max_num
#         # 
#         for i in range(m):
#             # Move pointer forward if current element is less than max_num
#             while indices[i] < n and matrix[i][indices[i]] < max_num:
#                 indices[i] += 1
#             # 
#             # If we moved out of bounds → no common element
#             if indices[i] == n:
#                 return -1
#             # 
#             # If current element is greater than max_num → update max_num and restart checking
#             if matrix[i][indices[i]] > max_num:
#                 max_num = matrix[i][indices[i]]
#                 break  # Restart loop with updated max_num
#             # 
#             # If current element equals max_num
#             if matrix[i][indices[i]] == max_num:
#                 count_equal += 1
#         # 
#         # If all rows are pointing to max_num → we found the common element
#         if count_equal == m:
#             return max_num


# def CreateMatrixWithAlternatingRectanglesOfOAndX(rows, columns):
#     """
#     """
#     matrix = [['X' for _ in range(columns)] for _ in range(rows)]
#     # print(matrix)
#     # 
#     top = left = 1
#     bottom = rows - 2
#     right = columns - 2
#     # 
#     while top <= bottom and left <= right:
#         matrix[top][left:right+1] = ['O' for _ in range(left, right+1)]
#         # 
#         if top + 1 <= bottom - 1:
#             for i in range(top+1, bottom):
#                 matrix[i][left] = matrix[i][right] = 'O'
#         # 
#         matrix[bottom][left:right+1] = ['O' for _ in range(left, right+1)]
#         # 
#         top += 2
#         left += 2
#         bottom -= 2
#         right -= 2
#     # 
#     # import pprint
#     # pprint.pprint(matrix)
#     # 
#     return matrix


# def maxArea(matrix):
#     """
#     https://www.geeksforgeeks.org/dsa/maximum-size-rectangle-binary-sub-matrix-1s/
#     2 aproches:
#         backtracking
#         histogram area - https://www.geeksforgeeks.org/dsa/largest-rectangular-area-in-a-histogram-using-stack/
#     using histogram approch
#     """
#     def maxHistogramArea(array, len_array):
#         """
#         https://www.geeksforgeeks.org/dsa/largest-rectangular-area-in-a-histogram-using-stack/
#         """
#         last_smaller = [-1]*len_array
#         next_smaller = [len_array]*len_array
#         # 
#         stack = []
#         for i in range(0,len_array):
#             while stack and array[stack[-1]] > array[i]:
#                 next_smaller[stack.pop()] = i
#             # 
#             if stack:
#                 last_smaller[i] = stack[-1]
#             # 
#             stack.append(i)
#         # 
#         max_area = 0
#         for i in range(0, len_array):
#             width = next_smaller[i] - last_smaller[i] - 1
#             current_area = array[i]*width
#             max_area = max(max_area, current_area)
#         # 
#         return max_area
#     # 
#     rows = len(matrix)
#     columns = len(matrix[0])
#     # 
#     max_area = 0
#     histogram_array = [0]*columns
#     for row in matrix:
#         for i in range(0, columns):
#             if row[i] == 1:
#                 histogram_array[i] += 1
#             else:
#                 histogram_array[i] = 0
#         # 
#         current_area = maxHistogramArea(array=histogram_array, len_array=columns)
#         max_area = max(max_area, current_area)
#     # 
#     return max_area


