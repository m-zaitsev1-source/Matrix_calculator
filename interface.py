from tkinter import *
from unittest import case
from matrix import *

def translate(txt: str):
    #txt = "E{3,3} + E{3,3}"
    #txt = "M{(1,2,3); (4,5,6)} + M{(1,2,3); (4,5,6)}"
    if 'M' not in txt and 'Z' not in txt and 'E' not in txt and 'V' not in txt:
        if txt != "":
            return str(eval(txt))
        return ""
    b = []
    k = 0
    is_first = True
    while k < len(txt):
        m = None
        if txt[k] == "M":
            o = k
            while txt[o] != '}':
                o += 1
            word = txt[k:o+1] # "M{(1,2,3); (4,5,6)}"
            l = word[2:-1].split('; ') # ['(1,2,3)', '(4,5,6)']
            for i in range(len(l)):
                l[i] = l[i][1:-1].split(',') # [['1', '2', '3'], ['4', '5', '6']]
                for j in range(len(l[i])):
                    l[i][j] = int(l[i][j])
            m = create_empty(len(l), len(l[0]))
            m.data = l
            if txt[k-1] == 't':
                m = transpose(m)
            k = o
        elif txt[k] == "Z":
            o = k
            while txt[o] != '}':
                o += 1
            word = txt[k:o+1] # "Z{3,3}"
            size = word[2:-1].split(',') # ['3', '3']
            m = create(int(size[0]), int(size[1]))
            k = o
        elif txt[k] == "E":
            o = k
            while txt[o] != '}':
                o += 1
            word = txt[k:o+1] # "E{3,3}"
            size = word[2:-1].split(',') # ['3', '3']
            m = create_identity(int(size[0]), int(size[1]))
            k = o
        elif txt[k] == "V":
            o = k 
            while txt[o] != '}':
                o += 1
            word = txt[k:o+1] # "V{3}"
            size = word[2:-1].split(',') # ['3']
            m = create_vector(int(size[0]))
            k = o
        elif txt[k] in '+-*/' or txt[k].isdigit():
            m = txt[k]
        elif txt[k] in '(':
            is_first = True
        elif txt[k] in ')':            
            is_first = False
        if m is not None:
            if is_first:
                b.append(m)
            else:
                b = [m] + b
        k += 1
    if len(b) == 2:
        raise NotImplementedError("Операция пока не реализована")
    while len(b) > 1:
        a1 = b.pop()
        a2 = b.pop()
        a3 = b.pop()
        if type(a1) == Matrix and type(a3) == Matrix:
            match a2:
                case '+':
                    b.append(add(a1, a3))
                case '-':
                    b.append(subtract(a1, a3))
                case '*':
                    b.append(multiply(a3, a1))
        elif type(a1) == Matrix and type(a3) == str:
            match a2:
                case '*':
                    b.append(multiply_scalar(a1, float(a3)))
                case '+':
                    b.append(add(a1, create_constants(a1.row, a1.col, float(a3))))
                case '-':
                    b.append(subtract(a1, create_constants(a1.row, a1.col, float(a3))))
        elif type(a1) == str and type(a3) == Matrix:
            match a2:
                case '*':
                    b.append(multiply_scalar(a3, float(a1)))
                case '+':
                    b.append(add(create_constants(a3.row, a3.col, float(a1)), a3))
                case '-':
                    b.append(subtract(create_constants(a3.row, a3.col, float(a1)), a3))
            pass
    return to_string(b[0])

def answer(txt):
    new_win = Tk()
    new_win.title("")
    new_win.geometry('200x200')
    text = translate(txt.get())
    l = Label(new_win, text=text, font="Arial 10", fg="blue")
    
    l.grid(column=0, row=0)

def help():
    new_win = Tk()
    new_win.title("Помощь")
    new_win.geometry('400x400')
    text = "Поддерживаемые операции:\n"
    text += "Сложение: M{(1,2); (3,4)} + M{(5,6); (7,8)}\n"
    text += "Умножение на скаляр: M{(1,2); (3,4)} * 2\n"
    text += "Умножение матриц: M{(1,2); (3,4)} * M{(5,6); (7,8)}\n"
    text += "Транспонирование: tM{(1,2); (3,4)}'\n"
    text += "Создание нулевой матрицы 3x3: Z{3,3}\n"
    text += "Создание единичной матрицы 3x3: E{3,3}\n"
    text += "Создание вектора-строки 1x3: V{ 3 }\n"
    l = Label(new_win, text=text, font="Arial 10", fg="blue")
    l.grid(column=0, row=0)
    new_win.mainloop()

def main():
    win = Tk()
    win.title("ыыыы")
    win.geometry('800x800')
    #это свобода
    bt1 = Button(win, text="Нажми меня", font="Arial 10", command=lambda: answer(txt))
    bt1.grid(column=1, row=0)
    txt = Entry(win, width=100)
    txt.grid(column=0, row=0)
    bt2 = Button(win, text="Очистить", font="Arial 10", command=lambda: txt.delete(0, END))
    bt2.grid(column=2, row=0)
    bt3 = Button(win, text="Помощь", font="Arial 10", command=help)
    bt3.grid(column=3, row=0)
    win.mainloop()
main()