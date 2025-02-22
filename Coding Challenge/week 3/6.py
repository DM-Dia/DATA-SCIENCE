def spiralOrder(m):
    if not m or not m[0]:
        return []

    res = []
    top, bottom = 0, len(m) - 1
    left, right = 0, len(m[0]) - 1

    while top <= bottom and left <= right:
        # Traverse from left to right
        for i in range(left, right + 1):
            res.append(m[top][i])
        top += 1  # Move down the top boundary

        # Traverse from top to bottom
        for i in range(top, bottom + 1):
            res.append(m[i][right])
        right -= 1  # Move left the right boundary

        if top <= bottom:
            # Traverse from right to left
            for i in range(right, left - 1, -1):
                res.append(m[bottom][i])
            bottom -= 1  # Move up the bottom boundary

        if left <= right:
            # Traverse from bottom to top
            for i in range(bottom, top - 1, -1):
                res.append(m[i][left])
            left += 1  # Move right the left boundary

    return res

# Test Cases
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix1))  # Output: [1,2,3,6,9,8,7,4,5]

matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix2))  # Output: [1,2,3,4,8,12,11,10,9,5,6,7]