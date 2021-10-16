import matplotlib.pyplot as plt
import numpy as np
from parser_points import parser

def partparab(x, y, t): 
    z = 0
    for i in range(len(x)-1):
        if t >= x[i] and t <= x[i+1]:
            M = np.array(
                [[x[i-1]**2, x[i-1], 1], [x[i]**2, x[i], 1], [x[i+1]**2, x[i+1], 1]])
            v = np.array([y[i-1], y[i], y[i+1]])
            solve = np.linalg.solve(M, v)  # [a, b, c]
            z = solve[0]*t**2 + solve[1]*t + solve[2]
        i += 1
    return z

def show_parab(i, i2):
    list_of_points = parser()
    for points in list_of_points[i:i2]:
        x = sorted(np.array(points[0], dtype=float))
        y = sorted(np.array(points[1], dtype=float))
        xnew = np.linspace(np.min(x), np.max(x), 100)
        ynew = [partparab(x, y, i) for i in xnew]
        plt.plot(xnew, ynew)
        plt.scatter(x, y)
    plt.show()