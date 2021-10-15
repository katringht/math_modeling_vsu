import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
from parser_points import parser

def spline(i, i2):
    list_of_points = parser()
    for points in list_of_points[i:i2]:
        x = sorted(np.array(points[0], dtype=float))
        y = sorted(np.array(points[1], dtype=float))
        tck = interpolate.splrep(x, y, k = 2)
        xi = np.linspace(np.min(x), np.max(x))
        fx = interpolate.splev(xi, tck)
        plt.plot(xi, fx)
        plt.scatter(x, y)
    plt.show()