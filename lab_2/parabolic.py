import matplotlib.pyplot as plt
import numpy as np
from parser_points import parser

def show_piecewise_parabolic_charts(file):
    list_of_points = parser(file)
    for points in list_of_points:
        x = np.array(points[0], dtype=float)
        y = np.array(points[1], dtype=float)
        a0 = []
        a1 = []
        a2 = []
        for i in range(1, len(x)-1):
            a2.append(((y[i+1]-y[i - 1])/((x[i + 1] - x[i - 1])*(x[i + 1] - x[i]))) - ((y[i] - y[i - 1])/((x[i] - x[i - 1])*(x[i + 1]-x[i]))))
            a1.append((y[i] - y[i - 1] - (a2[i-1] * ((x[i] ** 2) - (x[i - 1] ** 2)))) / (x[i] - x[i - 1]))
            a0.append(y[i - 1] - (a1[i-1] * x[i - 1]) - (a2[i-1] * (x[i - 1] ** 2)))
            
        for i in range(0, len(x)-2, 2):
            xi = np.linspace(x[i], x[i+2])
            f = a0[i] + a1[i]*xi + a2[i]*xi*xi
            plt.plot(xi, f)
        plt.scatter(x, y)
    plt.show()