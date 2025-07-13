def diagonalTraversal(array):
    """
    """
    col = len(array)
    row = len(array[0])
    diagonal_item = []
    for i in range(0,row):
        for j in range(0,i+1):
            diagonal_item.append(array[i][j])
            i -= 1
    # 
    return diagonal_item 


arr =   [[ 1, 2, 3, 4 ],
        [5, 6, 7, 8 ],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
        [17, 18, 19, 20]]

print(diagonalTraversal(array=arr))