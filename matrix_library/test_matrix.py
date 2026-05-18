import matrix
def print_matrix(mat):
    """Print matrix in readable format."""
    for i in range(mat.row):
        print(mat.data[i])
a1 = matrix.create(2, 3)
print("Matrix a1:")
print_matrix(a1)
a2 = matrix.create_identity(4, 4)
print("\nMatrix a2 (Identity):")
print_matrix(a2)
a3 = matrix.create_constants(3, 4, 5.0)
print("\nMatrix a3 (Constants):")
print_matrix(a3)