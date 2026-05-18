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

def resize(mat: Matrix, rows: int, cols: int):
    """Resize existing matrix, fill new elements with zeros (if new dimensions greater than current)."""
    ...

def get_element(mat: Matrix, rowIdx: int, colIdx: int):
    """Get element at specified position."""
    ...

def set_element(mat: Matrix, rowIdx: int, colIdx: int, value: float):
    """Set element at specified position."""
    ...

def set_identity(mat: Matrix):
    """Transform matrix into identity (square part only)."""
    ...

def set_zero(mat: Matrix):
    """Fill matrix with zeros."""
    ...

def set_constants(mat: Matrix, value: float):
    """Fill matrix with constant value."""
    ...

def transpose(mat: Matrix):
    """Return transposed matrix."""
    ...

def inverse(mat: Matrix):
    """Returns inverse matrix (square only)."""
    ...

def determinant(mat: Matrix):
    """Returns determinant of matrix (square only)."""
    ...