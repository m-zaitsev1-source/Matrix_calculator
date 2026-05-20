import matrix
def print_matrix(mat):
    """Print matrix in readable format."""
    for i in range(mat.row):
        print(mat.data[i])
a1 = matrix.create(3, 3)
print_matrix(a1)
a1.data = [[0, 0, 1], [5,4,3], [2, 1, 0]]
a2 = matrix.staircase(a1)
print_matrix(a2)