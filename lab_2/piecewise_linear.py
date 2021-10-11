import matplotlib.pyplot as plt
import numpy as np
from parser_points import parser

def piecewise_linear(x, y, xi):
    yx = 0
    for i in range(len(x)):
        if x[i - 1] <= xi <= x[i]:
            yp = y[i] - y[i - 1]
            xp = x[i] - x[i - 1]
            yx = y[i] + ((yp / xp) * (xi - x[i]))
            break
    return yx

def  show_piecewise_linear(file):
    list_of_points = parser(file)
    for points in list_of_points:
        x = np.array(points[0], dtype=float)
        y = np.array(points[1], dtype=float)
        t = [piecewise_linear(x, y, i) for i in x]
        plt.plot(x, y)
        plt.scatter(x, t)
    plt.grid(True)
    plt.show()
