matrix_example = [
          [1, 5, 4],
          [4, 2, -2],
          [7, 65, 88]
]

def even_numbers_in_matrix(matrix):
    num_of_even = 0
    for i in range( len (matrix) ):
        for j in range( len (matrix[i]) ):
            if matrix[i][j]%2 == 0:
                num_of_even = num_of_even + 1
    
    return num_of_even

print(even_numbers_in_matrix(matrix_example))