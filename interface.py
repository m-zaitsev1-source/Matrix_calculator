from tkinter import *
from libraries.matrix import *
from tkinter import messagebox
from math import *
from translate import *
history = []
def answer(txt):
    new_win = Tk()
    new_win.title("")
    new_win.geometry('200x200')
    new_win.resizable(False, False)
    try:
        result = translate(txt.get())
        history.append((result))
        l = Label(new_win, text=to_string(result), font="Arial 10", fg="blue")
        l.grid(column=0, row=0)
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))
        new_win.destroy()

def help():
    """Вывод окна с подсказкой"""
    new_win = Tk()
    new_win.title("Помощь")
    new_win.geometry('500x300')
    new_win.resizable(False, False)
    new_win.columnconfigure(0, weight=1)
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
    text += "Отрицательные числа берутся в скобки"
    l = Label(new_win, text=text, font="Arial 15", fg="blue")
    l.grid(column=0, row=0, sticky="nsew")
    new_win.mainloop()

def insert_matrix(txt, factor):
    """Вставка матрицы в текстовое поле, factor - тип вставляемой матрицы (M, E, Z)"""
    def on_closing():
        if factor == "M":
            st = "M{" + ((("("+("0 "*col_scale.get())[:-1] +")")+",")*row_scale.get())[:-1] + "}"
        elif factor == "E":
            st = "E{" + str(row_scale.get()) + "," + str(col_scale.get()) + "}"
        elif factor == "Z":
            st = "Z{" + str(row_scale.get()) + "," + str(col_scale.get()) + "}"
        elif factor == "V":
            st = "V{" + ("0 "*col_scale.get())[:-1] + "}"
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

def show_history():
    """Показать историю вычислений"""
    new_win = Tk()
    new_win.title("История")
    new_win.geometry('200x200')
    new_win.columnconfigure(0, weight=1)
    text = ""
    if history == []:
        text = "История пуста"
    else:
        l = len(history)
        for i in range(l - 1, -1, -1):
            text += str(l-i) + ") " + to_string(history[i]) + "\n\n"
    l = Label(new_win, text=text, font="Arial 10", fg="blue")
    l.grid(column=0, row=0)
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
    history_menu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Файл", menu=file_menu)
    menu.add_cascade(label="Помощь", command=help)
    menu.add_cascade(label="Вставить", menu=insert_menu)
    menu.add_cascade(label="История", menu=history_menu)
    file_menu.add_command(label="Выход", command=win.quit)
    insert_menu.add_command(label="Вставить матрицу", command=lambda: insert_matrix(txt, "M"))
    insert_menu.add_command(label="Вставить единичную матрицу", command=lambda: insert_matrix(txt, "E"))
    insert_menu.add_command(label="Вставить нулевую матрицу", command=lambda: insert_matrix(txt, "Z"))
    history_menu.add_command(label="Показать историю", command=show_history)
    history_menu.add_command(label="Очистить историю", command=lambda: history.clear())
    history_menu.add_command(label="Вставить ответ из истории", command=lambda: txt.insert(END, translate_back(history[-1]) if history else ""))
    history_menu.add_command(label="Удалить последний ответ", command=lambda: history.pop() if history else None)
    win.config(menu=menu)
    win.mainloop()
main()