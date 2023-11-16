
matrix_example = [
          [1, 5, 4],
          [4, 2, -2],
          [7, 65, 88]
]




def matrix_sum(matrix1, matrix2):
    result = []
    for i, row in enumerate(matrix1):
        r = []
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]): 
            print('Error! Matrices dimensions are different!')
            return
        else:
            for j, x in enumerate(row): 
                r.append(x + matrix2[i][j])
        result.append(r)
    return result

print(matrix_sum(matrix_example, matrix_example))


