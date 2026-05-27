import libraries.matrix as matrix
def print_matrix(mat):
    """Print matrix in readable format."""
    for i in range(mat.row):
        print(mat.data[i])
a1 = matrix.create(3, 3)
a1.data = [[1, 1/2, 1/3], [1/2,1/3,1/4], [1/3,1/4,1/5]]
print(matrix.is_valid(a1))
print(matrix.determinant(a1))