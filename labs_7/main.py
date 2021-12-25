import matplotlib.pyplot as plt
import numpy as np

from dichotomy_method import *
from equations import *
from hord_method import *
from newton_method import *
# from alittleparty import *
from plot import *
from simple_iteration_method import *


# Вводим начальные значения
a = float(input("Параметр a: "))
b = float(input("Параметр b: "))

intervalA = float(input("Левая граница интервала: "))
intervalB = float(input("Правая граница интервала: "))

# Строим график функций для наглядности
x = np.linspace(intervalA, intervalB, 1000)
y1 = fun(a, b, x)

plt.plot(x, y1)
plt.plot(x, [0 for x in x])
plt.grid(True)
plt.show()

x0 = float(input("Начальное приближение x0: "))
eps = 0.001

# Узнаем количество знаков после запятой
s = str(eps)
number = abs(s.find('.') - len(s)) - 1

n = int(input("Число итераций n: "))

print("\n-----------------------------------------------------------------")

print("\nМЕТОД ДИХОТОМИИ")
dichotomy_method(eps, number, a, b, intervalA, intervalB)
create_plot(x, y1, [0 for _ in x], "Метод дихотомии")

print("\nМЕТОД ПРОСТЫХ ОПЕРАЦИЙ")
iteration_method(x0, eps, number, a, b)
create_plot(x, y1, [0 for _ in x], "Метод простых итераций")

print("\nМЕТОД НЬЮТОНА")
newton_method(x0, n, a, b, eps, number)
create_plot(x, y1, [0 for _ in x], "Метод Ньютона")

print("\nМЕТОД ХОРД")
hord_method(x0, n, a, b, eps, number)
create_plot(x, y1, [0 for _ in x], "Метод хорд")

