from libraries.matrix import *
from math import *
from translate import *

#1 Сложение матриц
txt = "M{(1 2),(3 4)} + M{(5 6),(7 8)}"
assert translate_back(translate(txt)) == "M{(6.0 8.0),(10.0 12.0)}"
txt = "M{(1 2),(3 4)} + 1"
assert translate_back(translate(txt)) == "M{(2.0 3.0),(4.0 5.0)}"
txt = "M{(1 2),(3 4)} + M{(5 6),(7 8)} + M{(1 1),(1 1)}"
assert translate_back(translate(txt)) == "M{(7.0 9.0),(11.0 13.0)}"
txt = "M{(1 2),(3 4)} + M{(5 6),(7 8)} + M{(1 1),(1 1),(1 1)}"
assert translate_back(translate(txt)) == "M{(7.0 9.0),(11.0 13.0),(1.0 1.0)}"
#2 Умножение на скаляр
txt = "M{(1 2),(3 4)} * 2"
assert translate_back(translate(txt)) == "M{(2.0 4.0),(6.0 8.0)}"
txt = "2 * M{(1 2),(3 4)}"
assert translate_back(translate(txt)) == "M{(2.0 4.0),(6.0 8.0)}"
txt = "M{(1 2),(3 4)} * 0"
assert translate_back(translate(txt)) == "M{(0.0 0.0),(0.0 0.0)}"
txt = "0 * M{(1 2),(3 4)}"
assert translate_back(translate(txt)) == "M{(0.0 0.0),(0.0 0.0)}"
txt = "M{(1 2),(3 4)} * (-1)"
assert translate_back(translate(txt)) == "M{(-1.0 -2.0),(-3.0 -4.0)}"
txt = "(-1) * M{(1 2),(3 4)}"
assert translate_back(translate(txt)) == "M{(-1.0 -2.0),(-3.0 -4.0)}"
#3 Умножение матриц
txt = "M{(1 2),(3 4)} * M{(5 6),(7 8)}"
assert translate_back(translate(txt)) == "M{(19.0 22.0),(43.0 50.0)}"
txt = "M{(1 2),(3 4)} * M{(5 6),(7 8)} * M{(1 0),(0 1)}"
assert translate_back(translate(txt)) == "M{(19.0 22.0),(43.0 50.0)}"
txt = "M{(5 6),(7 8)} * M{(1 2),(3 4)}"
assert translate_back(translate(txt)) == "M{(23.0 34.0),(31.0 46.0)}"
txt = "M{(1 2),(3 4)} * M{(5 6),(7 8)} * M{(1 2),(3 4)}"
assert translate_back(translate(txt))  == "M{(85.0 126.0),(193.0 286.0)}"
#4 Транспонирование
txt = "tM{(1 2),(3 4)}'"
assert translate_back(translate(txt)) == "M{(1.0 3.0),(2.0 4.0)}"
txt = "tM{(1 2 3),(4 5 6)}'"
assert translate_back(translate(txt)) == "M{(1.0 4.0),(2.0 5.0),(3.0 6.0)}"
txt = "tM{(1 2),(3 4),(5 6)}'"
assert translate_back(translate(txt)) == "M{(1.0 3.0 5.0),(2.0 4.0 6.0)}"
#5 Обратная матрица и детерминант
txt = "dM{(1 2),(3 4)}'"
assert translate_back(translate(txt)) == "-2.0"
txt = "iM{(1 2),(3 4)}'"
assert translate_back(translate(txt)) == "M{(-0.5 -0.0),(-1.0 1.0)}"