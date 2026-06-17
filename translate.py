from libraries.matrix import *
from math import *
def translate(txt: str):
    """Перевод строки в результат вычисления"""
    if 'M' not in txt and 'Z' not in txt and 'E' not in txt and 'V' not in txt:
        if txt != "":
            return str(eval(txt))
        return ""
    stack = []
    k = 0
    while k < len(txt):
        m = None
        # обычная матрица
        if txt[k] == "M":
            o = k
            while txt[o] != '}':
                o += 1
            word = txt[k:o+1] # "M{(1 2 3),(4 5 6)}"
            l = word[2:-1].split(',') # ['(1 2 3)', '(4 5 6)']
            for i in range(len(l)):
                l[i] = l[i][1:-1].split(' ') # [['1', '2', '3'], ['4', '5', '6']]
                for j in range(len(l[i])):
                    l[i][j] = int(l[i][j])
            m = create_empty(len(l), len(l[0]))
            m.data = l
            if txt[k-1] == 't':
                m = transpose(m)
            if txt[k-1] == "d":
                m = determinant(m)
            if txt[k-1] == "i":
                m = invert(m)
            k = o
        # 0-матрица
        elif txt[k] == "Z":
            o = k
            while txt[o] != '}':
                o += 1
            word = txt[k:o+1] # "Z{3,3}"
            size = word[2:-1].split(',') # ['3', '3']
            m = create(int(size[0]), int(size[1]))
            k = o
        # единичная матрица
        elif txt[k] == "E":
            o = k
            while txt[o] != '}':
                o += 1
            word = txt[k:o+1] # "E{3,3}"
            size = word[2:-1].split(',') # ['3', '3']
            m = create_identity(int(size[0]), int(size[1]))
            if txt[k-1] == 't':
                m = m
            if txt[k-1] == "d":
                m = 1
            if txt[k-1] == "i":
                m = m
            k = o
        # вектор-строка
        elif txt[k] == "V":
            o = k 
            while txt[o] != '}':
                o += 1
            word = txt[k:o+1] # "V{1,2,3}"
            inside = word[2:-1].split(',') # ['1', '2', '3']
            m = create_vector(len(inside))
            m.data = [[int(i) for i in inside]]
            if txt[k-1] == 't':
                m = transpose(m)
            k = o
        elif txt[k] in '+-*/' or txt[k].isdigit():
            m = txt[k]
        elif txt[k] in '(':
            o = k
            while txt[o] != ')':
                o += 1
            m = txt[k+1:o]
            k = o
        if m is not None:
            stack = [m] + stack
        k += 1
    if len(stack) == 2:
        raise Exception("Неверный формат выражения")
    while len(stack) > 1:
        a1 = stack.pop()
        a2 = stack.pop()
        a3 = stack.pop()
        if type(a1) == Matrix and type(a3) == Matrix:
            match a2:
                case '+':
                    stack.append(add(a1, a3))
                case '-':
                    stack.append(subtract(a1, a3))
                case '*':
                    stack.append(multiply(a1, a3))
        elif type(a1) == Matrix and type(a3) == str:
            match a2:
                case '*':
                    stack.append(multiply_scalar(a1, float(a3)))
                case '+':
                    stack.append(add(a1, create_constants(a1.row, a1.col, float(a3))))
                case '-':
                    stack.append(subtract(a1, create_constants(a1.row, a1.col, float(a3))))
                case '/':
                    stack.append(divide_scalar(a1, create_constants(a1.row, a1.col, float(a3))))
        elif type(a1) == str and type(a3) == Matrix:
            match a2:
                case '*':
                    stack.append(multiply_scalar(a3, float(a1)))
                case '+':
                    stack.append(add(create_constants(a3.row, a3.col, float(a1)), a3))
                case '-':
                    stack.append(subtract(create_constants(a3.row, a3.col, float(a1)), a3))
                case '/':
                    stack.append(divide_scalar(a3, float(a1)))
            pass
    return stack[0]

def to_string(mat):
    """Строчное представление матрицы/числа."""
    if not isinstance(mat, Matrix):
        return str(mat)
    if not is_valid(mat):
        raise ValueError("Invalid matrix")
    s = ""
    for i in range(mat.row):
        s += "( "
        for j in range(mat.col):
            s += str(mat.data[i][j])
            if j < mat.col - 1:
                s += " , "
        s += " )"
        if i < mat.row - 1:
            s += ";\n"
    return s

def translate_back(mat):
    """Перевод матрицы в строку для вставки в текстовое поле."""
    s = "M{"
    for i in range(mat.row):
        s += "("
        for j in range(mat.col):
            s += str(mat.data[i][j])
            if j < mat.col - 1:
                s += " "
        s += ")"
        if i < mat.row - 1:
            s += ","
    s += "}"
    return s
