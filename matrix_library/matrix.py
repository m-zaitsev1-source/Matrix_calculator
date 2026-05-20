class Matrix:
    """Matrix itself. Stores data as 1D list and keeps dimensions."""
    col: int
    row: int
    data: list[float]
    pass

def create_empty():
    """Create empty matrix."""
    m = Matrix()
    m.row = 0
    m.col = 0
    m.data = []
    return m
    ...

def create_vector(cols):
    """Create row vector (1 x cols) filled with zeros."""
    m = Matrix()
    m.row = 1
    m.col = cols
    m.data = [0.0] * cols
    return m

def create(rows, cols):
    """Create matrix with given dimensions filled with zeros."""
    m = Matrix()
    m.row = rows
    m.col = cols
    m.data = [[0.0]*cols for _ in range(rows)]
    return m

def create_identity(rows, cols):
    """Create identity matrix (with min(rows,cols) ones on diagonal)."""
    m = create(rows, cols)
    for i in range(min(rows, cols)):
        m.data[i][i] = 1.0
    return m

def create_constants(rows, cols, value):
    """Create matrix filled with constant value."""
    m = create(rows, cols)
    for i in range(rows):
        for j in range(cols):
            m.data[i][j] = value
    return m

def is_valid(mat: Matrix):
    """Check if matrix has valid dimensions and data."""
    if mat.col*mat.row != len(mat.data):
        return False
    return True
    ...

def copy(mat: Matrix):
    """Create deep copy of matrix."""
    m = Matrix()
    m.row = mat.row
    m.col = mat.col
    m.data = mat.data.copy()
    return m
    ...

def destroy(mat: Matrix):
    """Clear matrix data and mark as empty. Returns matrix"""
    mat.row = 0
    mat.col = 0
    mat.data = []
    return mat

def multiply(mat1: Matrix, mat2: Matrix):
    """Returns new matrix (similarly in the methods below), the result of (mat1 * mat2)."""
    if mat1.col != mat2.row:
        raise ValueError("Incompatible dimensions for multiplication")
    new_mat = create(mat1.row, mat2.col)
    for i in range(mat1.row):
        for j in range(mat2.col):
            sum = 0.0
            for k in range(mat1.col):
                sum += mat1.data[i][k] * mat2.data[k][j]
            new_mat.data[i][j] = sum
    return new_mat

def subtract(mat1: Matrix, mat2: Matrix):
    """Returns the result of (mat1 - mat2)."""
    new_mat = create(mat1.row, mat1.col)
    for i in range(mat1.row):
        for j in range(mat1.col):
            new_mat.data[i][j] = mat1.data[i][j] - mat2.data[i][j]
    return new_mat
    ...

def add(mat1: Matrix, mat2: Matrix):
    """Returns the result of (mat1 + mat2)."""
    new_mat = create(mat1.row, mat1.col)
    for i in range(mat1.row):
        for j in range(mat1.col):
            new_mat.data[i][j] = mat1.data[i][j] + mat2.data[i][j]
    return new_mat
    ...

def multiply_scalar(mat: Matrix, value: float):
    """Multiply matrix by scalar."""
    new_mat = create(mat.row, mat.col)
    for i in range(mat.row):
        for j in range(mat.col):
            new_mat.data[i][j] = mat.data[i][j] * value
    return new_mat

def divide_scalar(mat: Matrix, value: float):
    """Divide matrix by scalar."""
    new_mat = create(mat.row, mat.col)
    for i in range(mat.row):
        for j in range(mat.col):
            new_mat.data[i][j] = mat.data[i][j] / value
    return new_mat
    ...

def set_zero(mat: Matrix):
    if not is_valid(mat):
        raise ValueError("Invalid matrix")
    """Fill matrix with zeros."""
    for i in range(mat.row):
        for j in range(mat.col):
            mat.data[i][j] = 0.0

def set_constants(mat: Matrix, value: float):
    if not is_valid(mat):
        raise ValueError("Invalid matrix")
    """Fill matrix with constant value."""
    for i in range(mat.row):
        for j in range(mat.col):
            mat.data[i][j] = value

def transpose(mat: Matrix):
    """Return transposed matrix."""
    if not is_valid(mat):
        raise ValueError("Invalid matrix")
    new_mat = create(mat.col, mat.row)
    for i in range(mat.row):
        for j in range(mat.col):
            new_mat.data[j][i] = mat.data[i][j]
    return new_mat

def staircase(mat: Matrix):
    """Return row echelon form of matrix."""
    if not is_valid(mat):
        raise ValueError("Invalid matrix")
    new_mat = copy(mat)
    for i in range(new_mat.row-1):
        # Find pivot
        pivot = None
        for j in range(new_mat.col):
            if new_mat.data[i][j] != 0:
                pivot = j
                break
        if pivot is None:
            continue
        # Eliminate below
        for k in range(i+1, new_mat.row):
            factor = new_mat.data[k][pivot] / new_mat.data[i][pivot]
            if factor == 0:
                continue
            for j in range(pivot, new_mat.col):
                new_mat.data[k][j] -= factor * new_mat.data[i][j]
    an_mat = create(new_mat.row, new_mat.col)
    for i in range(an_mat.row):
        k = 0
        for j in range(new_mat.row):
            if new_mat.data[j][k] != 0:
                an_mat.data[i][k] = new_mat.data[j][k]
                new_mat.data[j] = [0.0] * new_mat.col
                k += 1
                break
    return an_mat


def determinant(mat: Matrix):
    """Returns determinant of matrix (square only)."""
    if not is_valid(mat):
        raise ValueError("Invalid matrix")
    if mat.row != mat.col:
        raise ValueError("Matrix must be square")
    ...