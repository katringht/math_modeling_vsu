import matplotlib.pyplot as plt
import numpy as np

from equations import fun


def hord_method(x0, iterations, a, b, eps, number):
    x = x0
    x1 = x0 + 2 * eps
    i = 0

    while np.abs(x - x1) >= eps and i < iterations:
        j = x1
        x1 = x - fun(a, b, x) / (fun(a, b, x) - fun(a, b, x1)) * (
                x - x1)
        x = j
        i += 1

    print("Число итераций: ", i)
    print("X: ", round(x, number))
    y = fun(a, b, x)
    plt.scatter(x, y, color="green")

