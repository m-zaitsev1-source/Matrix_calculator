
class Matrix:
    """Matrix itself. Stores data as 1D list and keeps dimensions."""
    col: int
    row: int
    data: list
    pass

def create_empty(rows, cols):
    """Create empty matrix."""
    m = Matrix()
    m.row = rows
    m.col = cols
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
        m.data[i][i] = 1
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
    if len(mat.data) != mat.row:
        return False 
    for i in range(mat.row):
        if len(mat.data[i]) != mat.col:
            return False
    return True

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

def _shtrassen_(mat1: Matrix, mat2: Matrix):
    """Algorithm: Strassen's."""
    k = 1
    while max(mat1.row, mat1.col, mat2.row, mat2.col) > 2**k:
        k+=1
    mat1 = extend(mat1, 2**k, 2**k)
    mat2 = extend(mat2, 2**k, 2**k)
    new_mat = create(2**k, 2**k)
    if k == 1:
        new_mat.data[0][0] = float(mat1.data[0][0] * mat2.data[0][0] + mat1.data[0][1] * mat2.data[1][0])
        new_mat.data[0][1] = float(mat1.data[0][0] * mat2.data[0][1] + mat1.data[0][1] * mat2.data[1][1])
        new_mat.data[1][0] = float(mat1.data[1][0] * mat2.data[0][0] + mat1.data[1][1] * mat2.data[1][0])
        new_mat.data[1][1] = float(mat1.data[1][0] * mat2.data[0][1] + mat1.data[1][1] * mat2.data[1][1])
        return new_mat
    else:
        A11 = create_empty(2**k//2, 2**k//2)
        A12 = create_empty(2**k//2, 2**k//2)
        A21 = create_empty(2**k//2, 2**k//2)
        A22 = create_empty(2**k//2, 2**k//2)
        B11 = create_empty(2**k//2, 2**k//2)
        B12 = create_empty(2**k//2, 2**k//2)
        B21 = create_empty(2**k//2, 2**k//2)
        B22 = create_empty(2**k//2, 2**k//2)
        A11.data = [[mat1.data[i][j] for j in range(mat1.col//2)] for i in range(mat1.row//2)]
        A12.data = [[mat1.data[i][j] for j in range(mat1.col//2, mat1.col)] for i in range(mat1.row//2)]
        A21.data = [[mat1.data[i][j] for j in range(mat1.col//2)] for i in range(mat1.row//2, mat1.row)]
        A22.data = [[mat1.data[i][j] for j in range(mat1.col//2, mat1.col)] for i in range(mat1.row//2, mat1.row)]
        B11.data = [[mat2.data[i][j] for j in range(mat2.col//2)] for i in range(mat2.row//2)]
        B12.data = [[mat2.data[i][j] for j in range(mat2.col//2, mat2.col)] for i in range(mat2.row//2)]
        B21.data = [[mat2.data[i][j] for j in range(mat2.col//2)] for i in range(mat2.row//2, mat2.row)]
        B22.data = [[mat2.data[i][j] for j in range(mat2.col//2, mat2.col)] for i in range(mat2.row//2, mat2.row)]
        D = _shtrassen_(add(A11, A22), add(B11, B22))
        D1 = _shtrassen_(subtract(A12, A22), add(B21, B22))
        D2 = _shtrassen_(subtract(A21, A11), add(B11, B12))
        H1 = _shtrassen_(add(A11, A12), B22)
        H2 = _shtrassen_(add(A21, A22), B11)
        V1 = _shtrassen_(A22, subtract(B21, B11))
        V2 = _shtrassen_(A11, subtract(B12, B22))
        C11 = add(add(D, D1), subtract(V1, H1))
        C12 = add(V2, H1)
        C21 = add(V1, H2)
        C22 = add(add(D, D2), subtract(V2, H2))
        for i in range(new_mat.row):
            for j in range(new_mat.col):
                if i < 2**(k-1) and j < 2**(k-1):
                    new_mat.data[i][j] = C11.data[i][j]
                elif i < 2**(k-1) and j >= 2**(k-1):
                    new_mat.data[i][j] = C12.data[i][j-2**(k-1)]
                elif i >= 2**(k-1) and j < 2**(k-1):
                    new_mat.data[i][j] = C21.data[i-2**(k-1)][j]
                elif i >= 2**(k-1) and j >= 2**(k-1):
                    new_mat.data[i][j] = C22.data[i-2**(k-1)][j-2**(k-1)]
        return new_mat

def multiply(mat1: Matrix, mat2: Matrix):
    """Returns the result of (mat1 * mat2)."""
    if mat1.col != mat2.row:
        raise ValueError("Матрицы не согласованы")
    new_mat = _shtrassen_(mat1, mat2)
    new_mat.data = [row[:mat2.col] for row in new_mat.data[:mat1.row]]
    new_mat.row = mat1.row
    new_mat.col = mat2.col
    return new_mat

def subtract(mat1: Matrix, mat2: Matrix):
    """Returns the result of (mat1 - mat2)."""
    new_mat = create(max(mat1.row, mat2.row), max(mat1.col, mat2.col))
    mat1 = extend(mat1, new_mat.row, new_mat.col)
    mat2 = extend(mat2, new_mat.row, new_mat.col)
    for i in range(mat1.row):
        for j in range(mat1.col):
            new_mat.data[i][j] = float(mat1.data[i][j]) - float(mat2.data[i][j])
    return new_mat
    ...
def extend(mat1: Matrix, new_rows, new_cols):
    """Extend matrix to new dimensions by adding zeros."""
    if mat1.row == new_rows and mat1.col == new_cols:
        return mat1
    if new_rows < mat1.row or new_cols < mat1.col:
        raise ValueError("New dimensions must be greater than current")
    new_mat = create(new_rows, new_cols)
    for i in range(mat1.row):
        for j in range(mat1.col):
            new_mat.data[i][j] = float(mat1.data[i][j])
    return new_mat

def add(mat1: Matrix, mat2: Matrix):
    """Returns the result of (mat1 + mat2)."""
    if not is_valid(mat1) or not is_valid(mat2):
        raise ValueError("Invalid matrix")
    new_mat = create(max(mat1.row, mat2.row), max(mat1.col, mat2.col))
    if mat1.row != new_mat.row or mat1.col != new_mat.col:
        mat1 = extend(mat1, new_mat.row, new_mat.col)
    if mat2.row != new_mat.row or mat2.col != new_mat.col:
        mat2 = extend(mat2, new_mat.row, new_mat.col)
    for i in range(mat1.row):
        for j in range(mat1.col):
            if mat1.data[i][j] == 0 and mat2.data[i][j] == 0:
                continue
            new_mat.data[i][j] = float(mat1.data[i][j]) + float(mat2.data[i][j])
    return new_mat
    ...

def multiply_scalar(mat: Matrix, value: float):
    """Multiply matrix by scalar."""
    new_mat = create(mat.row, mat.col)
    for i in range(mat.row):
        for j in range(mat.col):
            new_mat.data[i][j] = float(mat.data[i][j]) * value
    return new_mat

def divide_scalar(mat: Matrix, value: float):
    """Divide matrix by scalar."""
    if value == 0.0:
        raise ValueError("Cannot divide by zero")
    new_mat = create(mat.row, mat.col)
    for i in range(mat.row):
        for j in range(mat.col):
            new_mat.data[i][j] = float(mat.data[i][j]) / value
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
            new_mat.data[j][i] = float(mat.data[i][j])
    return new_mat

def staircase(new_mat: Matrix):
    """Return row echelon form of matrix."""
    if not is_valid(new_mat):
        raise ValueError("Invalid matrix")
    #Cначала считыем по Гауссу
    mat = copy(new_mat)
    for i in range(mat.row-1):
        # Нахожу ведущий элемент в строке
        pivot = None
        for j in range(mat.col):
            if mat.data[i][j] != 0:
                pivot = j
                break
        if pivot is None:
            continue
        # Привожу все строки ниже текущей к нулю в столбце ведущего элемента
        for k in range(i+1, mat.row):
            factor = mat.data[k][pivot] / mat.data[i][pivot]
            if factor == 0:
                continue
            for j in range(pivot, mat.col):
                mat.data[k][j] -= factor * mat.data[i][j]
    #Потом доводим по ЖОрдану
    an_mat = create(mat.row, mat.col)
    k = 0
    while k < mat.col: 
        for j in range(mat.row):
            if mat.data[j][k] != 0:
                an_mat.data[k][k] = mat.data[j][k]
                mat.data[j] = [0.0] * mat.col
                break
        k += 1
    return an_mat

def determinant(mat: Matrix):
    """Returns determinant of matrix (square only)."""
    if not is_valid(mat):
        raise ValueError("Invalid matrix")
    if mat.row != mat.col:
        raise ValueError("Matrix must be square")
    mat = staircase(mat)
    det = 1.0
    for i in range(mat.row):
        if mat.data[i][i] == 0:
            return 0.0
        det *= mat.data[i][i]
    return round(det, 4)

def invert(mat: Matrix) -> Matrix:
    d = determinant(mat)
    """Returns inverse of matrix (square only)."""
    if not is_valid(mat):
        raise ValueError("Invalid matrix")
    if d == 0:
        raise ValueError("Matrix is not invertible")
    return divide_scalar(transpose(mat), d)

