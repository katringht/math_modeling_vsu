import matplotlib.pyplot as plt

from equations import *


def iteration_method(x0, eps, number, a, b):
    x1 = phi(a, b, x0)
    x = x0
    n = 0
    while abs(x1 - x) >= abs(eps):
        x = x1
        x1 = phi(a, b, x)
        n += 1
        if abs(x - x1) < eps:
            break
    print("Число итераций: ", n)
    print("X: ", round(x1, number))
    y = fun(a, b, x1)
    plt.scatter(x1, y, color="green")
