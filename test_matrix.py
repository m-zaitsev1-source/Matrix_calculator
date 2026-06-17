import libraries.matrix as matrix
def print_matrix(mat):
    """Print matrix in readable format."""
    for i in range(mat.row):
        print(mat.data[i])

# проверка сложения матриц
a1 = matrix.create(2, 2)
a2 = matrix.create(3, 2)
a1.data = [[1, 2], [3, 4]]
a2.data = [[5, 6], [8, 9], [11, 12]]
a3 = matrix.add(a2, a1)

#проверка умножения матриц
a1 = matrix.create(2, 2)
a2 = matrix.create(2, 2)
a1.data = [[1, 2], [3, 4]]
a2.data = [[5, 6], [7, 8]]
a3 = matrix.multiply(a1, a2)
print_matrix(a3)
a3 = matrix.create(4, 4)
a4 = matrix.create(4, 4)
a3.data = [[1, 2, 3, 10], [4, 5, 6, 11], [7, 8, 9, 12], [16, 17, 18, 19]]
a4.data = [[1, 2, 3, 13], [4, 5, 6, 14], [7, 8, 9, 15], [16, 17, 18, 20]]
a5 = matrix.multiply(a3, a4)