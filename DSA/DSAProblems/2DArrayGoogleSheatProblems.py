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


def spiralOrder(matrix):
    """
    """
    total_row = len(matrix)
    total_col = len(matrix[0])
    # 







def spiralTraverse(matrix, row_no, col_no, total_row, total_col):
    """
    """
    traverse_list = []
    while i < total_col - row_no:





    traverse_list += matrix[current_row][current_col:total_col - current_col]






matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

print(setZeroes(matrix=matrix))

