import math
from my import monte_carlo_Second_method
from methods import *
from utils import *
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from numpy import std

#  1
y = lambda x: x * math.e / (1 + x)**2
a = 0.6
b = 6
fig = plt.subplots()
x = np.linspace(a, b, 100)
plt.plot(x, y(x))

# 2 
v, err = integrate.quad(y, a, b)
print("Аналитическое выражение I: ", round(v, 5))

def num_of_nodes(method, y, a, b):
    val = v
    i = 100
    n = 1
    temp = np.abs(method(y, a, b, n))
    while i > val:
        n *= 2
        i = np.abs(np.abs(method(y, a, b, n)) - temp) * 100 / val
        temp = method(y, a, b, n)
    return n


trap_nodes = num_of_nodes(trapezoid_rule, y, a, b)
t = trapezoid_rule(y, a, b, trap_nodes)
print("Метод трапеции: ", round(t, 3))
print("Количество узлов: ", round(trap_nodes, 3))

#3
m1_nodes = num_of_nodes(monte_carlo_1_method, y, a, b)
m1 = monte_carlo_1_method(y, a, b, m1_nodes)
print("Monte Carlo 1: ", round(m1, 3))
print("Выборочные среднеквадратичные отклонения: ", round(std([monte_carlo_1_method(y, a, b, m1_nodes) for _ in range(100)]), 3))
# print("Количество узлов: ", round(m1_nodes, 3))

m2_nodes = num_of_nodes(monte_carlo_Second_method, y, a, b)
m2 = monte_carlo_Second_method(y, a, b, m1_nodes)
print("Monte Carlo 2: ", round(m2, 3))
print("Выборочные среднеквадратичные отклонения: ", round(std([monte_carlo_Second_method(y, a, b, m2_nodes) for _ in range(100)]), 3))
# print("Количество узлов: ", round(m2_nodes, 3))
plt.show()
