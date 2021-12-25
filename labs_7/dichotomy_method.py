import matplotlib.pyplot as plt

from equations import *


def dichotomy_method(eps, number, a, b, intervalA, intervalB):
    x0 = (intervalB + intervalA) / 2
    n = 0
    while intervalB - intervalA >= 2 * eps:
        n += 1
        if fun(a, b, x0) == 0:
            break
        if fun(a, b, intervalA) * fun(a, b, x0) < 0:
            intervalB = x0
        elif fun(a, b, intervalB) * fun(a, b, x0) < 0:
            intervalA = x0
        x0 = (intervalB + intervalA) / 2
    print("Число итераций: ", n)
    print("X: ", round(x0, number))
    y = fun(a, b, x0)
    plt.scatter(x0, y, color="green")