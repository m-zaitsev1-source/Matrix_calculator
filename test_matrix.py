import matrix
def print_matrix(mat):
    """Print matrix in readable format."""
    for i in range(mat.row):
        print(mat.data[i])
a1 = matrix.create(3, 3)
a1.data = [[0, 0, 1], [5,4,3], [2, 1, 0]]
print(matrix.is_valid(a1))
print(matrix.determinant(a1))