from libraries.matrix import *
from math import *
from translate import *

#1 Сложение матриц
txt = "M{(1 2),(3 4)} + M{(5 6),(7 8)}"
assert translate_back(translate(txt)) == "M{(6 8),(10 12)}"
txt = "M{(1 2),(3 4)} + 1"
assert translate_back(translate(txt)) == "M{(2 3),(4 5)}"
txt = "M{(1 2),(3 4)} + M{(5 6),(7 8)} + M{(1 1),(1 1)}"
assert translate_back(translate(txt)) == "M{(7 9),(11 13)}"
txt = "M{(1 2),(3 4)} + M{(5 6),(7 8)} + M{(1 1),(1 1),(1 1)}"
assert translate_back(translate(txt)) == "M{(7 9),(11 13),(1 1)}"
#2 Умножение на скаляр
txt = "M{(1 2),(3 4)} * 2"
assert translate_back(translate(txt)) == "M{(2 4),(6 8)}"
txt = "2 * M{(1 2),(3 4)}"
assert translate_back(translate(txt)) == "M{(2 4),(6 8)}"
txt = "M{(1 2),(3 4)} * 0"
assert translate_back(translate(txt)) == "M{(0 0),(0 0)}"
txt = "0 * M{(1 2),(3 4)}"
assert translate_back(translate(txt)) == "M{(0 0),(0 0)}"
txt = "M{(1 2),(3 4)} * (-1)"
assert translate_back(translate(txt)) == "M{(-1 -2),(-3 -4)}"
txt = "(-1) * M{(1 2),(3 4)}"
assert translate_back(translate(txt)) == "M{(-1 -2),(-3 -4)}"
#3 Умножение матриц
txt = "M{(1 2),(3 4)} * M{(5 6),(7 8)}"
assert translate_back(translate(txt)) == "M{(19 22),(43 50)}"
txt = "M{(1 2),(3 4)} * M{(5 6),(7 8)} * M{(1 0),(0 1)}"
assert translate_back(translate(txt)) == "M{(19 22),(43 50)}"
txt = "M{(5 6),(7 8)} * M{(1 2),(3 4)}"
assert translate_back(translate(txt)) == "M{(23 34),(31 46)}"
