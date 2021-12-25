import matplotlib.pyplot as plt

from equations import *


def newton_method(x, n, a, b, eps, number):
    x1 = x
    # число итерций
    N = 0
    for _ in range(n):
        N += 1
        x1 = x - (fun(a, b, x) / derivative_fun(a, x))
        # Если разница между текущим корнем и предыдущим меньше eps
        if abs(x1 - x) < eps:
            break
        x = x1
    print("Число итераций: ", N)
    print("X: ", round(x1, number))
    y = fun(a, b, x1)
    plt.scatter(x1, y, color="green")
