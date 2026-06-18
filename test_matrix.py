import libraries.matrix as matrix
def print_matrix(mat):
    """Print matrix in readable format."""
    for i in range(mat.row):
        print([round(j, 4) for j in mat.data[i]])

# проверка сложения матриц
a1 = matrix.create(2, 2)
a2 = matrix.create(3, 2)
a1.data = [[1, 2], 
           [3, 4]]

a2.data = [[5, 6], 
           [8, 9], 
           [11, 12]]
a3 = matrix.add(a2, a1)
a1 = matrix.create(3,3)
a2 = matrix.create(2,2)
a1.data = [[1, 2, 4],
           [5, 6, 5],
           [8, 8, 8]]
a2.data = [[1, 2],
           [0, 0]]
a3 = matrix.add(a1, a2)
assert a3.data == [[2.0, 4.0, 4.0],
                   [5.0, 6.0, 5.0],
                   [8.0, 8.0, 8.0]]
#проверка умножения матриц
a1 = matrix.create(2, 2)
a2 = matrix.create(2, 2)
a1.data = [[1, 2], 
           [3, 4]]
a2.data = [[5, 6], 
           [7, 8]]
a3 = matrix.multiply(a1, a2)
assert a3.data == [[19.0, 22.0], 
                   [43.0, 50.0]]
a3 = matrix.create(4, 4)
a4 = matrix.create(4, 4)
a3.data = [[1, 2, 3, 10], 
           [4, 5, 6, 11], 
           [7, 8, 9, 12], 
           [16, 17, 18, 19]]
a4.data = [[1, 2, 3, 13], 
           [4, 5, 6, 14], 
           [7, 8, 9, 15], 
           [16, 17, 18, 20]]
a5 = matrix.multiply(a3, a4)
assert a5.data == [[190.0, 206.0, 222.0, 286.0],
                   [242.0, 268.0, 294.0, 432.0],
                   [294.0, 330.0, 366.0, 578.0],
                   [514.0, 584.0, 654.0, 1096.0]]
#проверка транспонирования
a6 = matrix.transpose(a1)
assert a6.data == [[1.0, 3.0], 
                   [2.0, 4.0]]
a7 = matrix.create(3, 2)
a7.data = [[1, 2], 
           [3, 4], 
           [5, 6]]
a8 = matrix.transpose(a7)
assert a8.data == [[1.0, 3.0, 5.0], 
                   [2.0, 4.0, 6.0]]
#проверка ступеней матрицы и оперделителя
a9 = matrix.create(3, 3)
a9.data = [[1, 2, 6], 
           [4, 5, 6], 
           [7, 8, 9]]
assert matrix.determinant(a9) == -9.0
a11 = matrix.create(4,4)
a11.data = [[1, 2, 3, 4], 
            [5, 6, 7, 7], 
            [9, 11, 11, 8], 
            [13, 14, 15, 16]]
assert matrix.determinant(a11) == 24.0
#проверка обратной матричы
a12 = matrix.create(3,2)
a12.data = [[1, 2, 3],
            [4, 5, 6]]
assert matrix.is_valid(a12) == False
a12 = matrix.create(2,3)
a12.data = [[1, 2, 3],
            [4, 5, 6]]
assert matrix.is_valid(a12) == True
a13 = matrix.create(3,3)
a13.data = [[1, 2, 3],
            [4, 0, 6],
            [7, 8, 9]]
print(matrix.determinant(a13))
print_matrix(matrix.invert(a13))
a14 = matrix.create_identity(3,3)
print(matrix.determinant(a14))