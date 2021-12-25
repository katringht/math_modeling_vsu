import math
from fibonacci import get_extremum_of_function_by_fibonacci_method
from golden import golden_ratio
from utils import get_M
import numpy as np
import matplotlib.pyplot as plt

y = lambda x: np.sin(x) / (2 * x)

a = int(input('Введите а: '))
b = int(input('Введите b: '))
eps = float(input('Введите точность: '))

qa = input('Задать число итераций для метода Фибоначчи [y/n]: ')
if qa == 'y':
    n = int(input('Введите n - число итераций: '))
else:
    n = None

x, fx, n = golden_ratio(y, a, b, eps)
fibx, fiby, n_f = get_extremum_of_function_by_fibonacci_method(y,a, b, eps, n)
print("Золотое Сечение")
print("Число итерайий: ", n)
print("Приблеженное значение Хm", x)
print("Значение функции Ym", fx)

print("Метод Фибоначи")
print("Число итераций: ", n_f)
print("Приблеженное значение Хm", fibx)
print("Значение функции Ym", fiby)

minim = get_M(a, b, y)
print("аналитический метод: ", round(minim, 3))
x = np.linspace(a, b, 1000)
plt.plot(x, y(x))
plt.show()

