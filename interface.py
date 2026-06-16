from tkinter import *
from libraries.matrix import *
from tkinter import messagebox
from math import *
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
            if txt[k-1] == 't':
                m = m
            if txt[k-1] == "d":
                m = 1
            if txt[k-1] == "i":
                m = m
            k = o
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
                case '/':
                    b.append(divide_scalar(a1, create_constants(a1.row, a1.col, float(a3))))
        elif type(a1) == str and type(a3) == Matrix:
            match a2:
                case '*':
                    b.append(multiply_scalar(a3, float(a1)))
                case '+':
                    b.append(add(create_constants(a3.row, a3.col, float(a1)), a3))
                case '-':
                    b.append(subtract(create_constants(a3.row, a3.col, float(a1)), a3))
                case '/':
                    b.append(divide_scalar(a3, int(a1)))
            pass
    return to_string(b[0])

def answer(txt):
    new_win = Tk()
    new_win.title("")
    new_win.geometry('200x200')
    new_win.resizable(False, False)
    try:
        text = translate(txt.get())
        l = Label(new_win, text=text, font="Arial 10", fg="blue")
        l.grid(column=0, row=0)
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))
        new_win.destroy()

def help():
    new_win = Tk()
    new_win.title("Помощь")
    new_win.geometry('300x200')
    text = "Поддерживаемые операции:\n"
    text += "Сложение: M{(1 2),(3 4)} + M{(5 6),(7 8)}\n"
    text += "Умножение на скаляр: M{(1 2),(3 4)} * 2\n"
    text += "Умножение матриц: M{(1 2),(3 4)} * M{(5 6),(7 8)}\n"
    text += "Транспонирование: tM{(1 2),(3 4)}'\n"
    text += "Создание нулевой матрицы 3x3: Z{3,3}\n"
    text += "Создание единичной матрицы 3x3: E{3,3}\n"
    text += "Создание вектора-строки (1,2,3): V{1 2 3}\n"
    text += "Определитель: dM{(1 2),(3 4)}\n"
    text += "Обратная матрица: iM{(1 2),(3 4)}\n"
    l = Label(new_win, text=text, font="Arial 10", fg="blue")
    l.grid(column=0, row=0)
    new_win.mainloop()

def insert_matrix(txt, factor):
    def on_closing():
        if factor == "M":
            st = "M{" + ((("("+("0 "*col_scale.get())[:-1] +")")+",")*row_scale.get())[:-1] + "}"
        elif factor == "E":
            st = "E{" + str(row_scale.get()) + "," + str(col_scale.get()) + "}"
        elif factor == "Z":
            st = "Z{" + str(row_scale.get()) + "," + str(col_scale.get()) + "}"
        txt.insert(END, st)
        new_win.destroy()
    new_win = Tk()
    new_win.title("Вставить матрицу")
    new_win.geometry('200x200')
    new_win.protocol("WM_DELETE_WINDOW", on_closing)
    new_win.columnconfigure(0, weight=1)
    label = Label(new_win, text="Выберите размер матрицы", font="Arial 10", fg="blue")
    label.grid(column=0, row=0, sticky="nsew")
    row_scale = Scale(new_win, from_=2, to=5, orient=HORIZONTAL, label="Строки")
    row_scale.grid(column=0, row=1)
    col_scale = Scale(new_win, from_=2, to=5, orient=HORIZONTAL, label="Столбцы")
    col_scale.grid(column=0, row=2)
    new_win.mainloop()

def main():
    win = Tk()
    win.title("Metrix")
    win.geometry('400x400')
    win.columnconfigure(0, weight=1)
    #кнопка =
    bt1 = Button(win, text="=", font="Arial 10", command=lambda: answer(txt))
    bt1.grid(column=1, row=0)
    #текстовое поле для ввода
    txt = Entry(win, width=30, font="Arial 20")
    txt.grid(column=0, row=0, sticky="nsew")
    txt.focus()
    bt2 = Button(win, text="Очистить", font="Arial 10", command=lambda: txt.delete(0, END))
    bt2.grid(column=2, row=0)
    menu = Menu(win)
    file_menu = Menu(menu, tearoff=0)
    insert_menu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Файл", menu=file_menu)
    menu.add_cascade(label="Помощь", command=help)
    menu.add_cascade(label="Вставить", menu=insert_menu)
    file_menu.add_command(label="Выход", command=win.quit)
    insert_menu.add_command(label="Вставить матрицу", command=lambda: insert_matrix(txt, "M"))
    insert_menu.add_command(label="Вставить единичную матрицу", command=lambda: insert_matrix(txt, "E"))
    insert_menu.add_command(label="Вставить нулевую матрицу", command=lambda: insert_matrix(txt, "Z"))
    win.config(menu=menu)
    win.mainloop()
main()