import libraries.matrix as matrix
def print_matrix(mat):
    """Print matrix in readable format."""
    for i in range(mat.row):
        print(mat.data[i])
a1 = matrix.create(2, 2)
a2 = matrix.create(2, 2)
a1.data = [[1, 2], [3, 4]]
a2.data = [[5, 6], [7, 8]]
a3 = matrix.multiply(a1, a2)
print_matrix(a3)
a3 = matrix.create(3, 3)
a4 = matrix.create(3, 3)
a3.data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a4.data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a5 = matrix.multiply(a3, a4)
print_matrix(a5)