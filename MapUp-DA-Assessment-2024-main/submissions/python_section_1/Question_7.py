# Question 7: Matrix Rotation and Transformation

import numpy as np
def rotate_matrix_90_clockwise(matrix):
    transposed = list(zip(*matrix))
    rotated = [list(row[::-1]) for row in transposed]
    return rotated
def transform_matrix(matrix):
    n = len(matrix)
    final_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            row_sum = sum(matrix[i]) - matrix[i][j]
            col_sum = sum(matrix[k][j] for k in range(n)) - matrix[i][j]
            final_matrix[i][j] = row_sum + col_sum
    
    return final_matrix
def rotate_and_transform(matrix):
    rotated_matrix = rotate_matrix_90_clockwise(matrix)
    final_matrix = transform_matrix(rotated_matrix)
    
    return final_matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
final_matrix = rotate_and_transform(matrix)
print(np.array(final_matrix))
