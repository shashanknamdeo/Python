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


def spiralOrder(self, matrix):
        """
        """
        total_row = len(matrix)
        total_col = len(matrix[0])
        # 
        traverse_list = []
        # 
        row_no = 0
        col_no = 0
        while (row_no < total_row//2 ) and (col_no < total_col//2):
            traverse_list += spiralTraverse(matrix=matrix, row_no=row_no, col_no=col_no, total_row=total_row, total_col=total_col)
            row_no += 1
            col_no += 1
        # 
        if total_row % 2 + total_col % 2 == 1:
            if total_row % 2 == 1:
                for i in range(col_no, total_col - col_no):
                    # print(1, 'row', i)
                    traverse_list.append(matrix[row_no][i])
            # 
            elif total_col % 2 == 1:
                for j in range(row_no, total_row - row_no):
                    # print(1, 'col', j)
                    traverse_list.append(matrix[j][col_no])
        # 
        if total_row % 2 + total_col % 2 == 2:
            # print(2)
            if total_row <= total_col:
                for i in range(col_no, total_col - col_no):
                    traverse_list.append(matrix[row_no][i])
            # 
            else:
                for j in range(row_no, total_row - row_no):
                    traverse_list.append(matrix[j][col_no])
        # 
        return traverse_list


def spiralTraverse(matrix, row_no, col_no, total_row, total_col):
    """
    """
    current_row = row_no
    current_col = col_no
    traverse_list = []
    # 
    traverse_list += matrix[current_row][current_col:total_col - current_col]
    current_col = total_col - current_col - 1
    # 
    j = current_row + 1
    while j < total_row - current_row:
        traverse_list.append(matrix[j][current_col])
        j += 1
    current_row = j - 1
    # 
    temp_array = matrix[current_row][col_no:current_col]
    temp_array.reverse()
    traverse_list += temp_array
    # 
    j = current_row - 1
    while j > row_no:
        traverse_list.append(matrix[j][col_no])
        j -= 1
    # 
    return traverse_list



def rotate(matrix):
    """
    make 4 array
    ht_array
    hb_array
    vl_array
    vr_array
    """














matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

print(rotate(matrix=matrix))
# print(spiralTraverse(matrix=matrix, row_no=0, col_no=0, total_row=3, total_col=4))
