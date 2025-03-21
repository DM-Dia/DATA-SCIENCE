def searchMatrix(mat, tar):
    if not mat or not mat[0]:
        return False

    m, n = len(mat), len(mat[0])
    row, col = 0, n - 1  # Start from top-right corner

    while row < m and col >= 0:
        if mat[row][col] == tar:
            return True
        elif mat[row][col] > tar:
            col -= 1  # Move left
        else:
            row += 1  # Move down

    return False

#test cases
mat1 = [[1,4,7,11,15],
           [2,5,8,12,19],
           [3,6,9,16,22],
           [10,13,14,17,24],
           [18,21,23,26,30]]

print(searchMatrix(mat1, 5))   # Output: True
print(searchMatrix(mat1, 20))  # Output: False