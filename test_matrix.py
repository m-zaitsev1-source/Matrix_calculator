import libraries.matrix as matrix
def print_matrix(mat):
    """Print matrix in readable format."""
    for i in range(mat.row):
        print(mat.data[i])
a1 = matrix.create(4, 4)
a1.data = [[60, 30, 20 , 25], [30, 20, 15, 17], [20, 15, 12, 13], [25, 17, 13, 17*6/7]]
a2 = matrix.create(3, 3)
a2.data = [[60, 30, 20], [30, 20, 15], [20, 15, 12]]
print(matrix.is_valid(a1))
print_matrix(matrix.staircase(a1))
print(matrix.is_valid(a2))
print_matrix(matrix.staircase(a2))
d1 = matrix.determinant(a1)
d2 = matrix.determinant(a2)
print(d2/d1)