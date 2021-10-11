import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
from parser_points import parser

def spline(file):
    list_of_points = parser(file)
    for points in list_of_points:
        x = np.array(points[0], dtype=float)
        y = np.array(points[1], dtype=float)
        tck = interpolate.splrep(x, y)
        xi = np.linspace(np.min(x), np.max(x))
        fx = interpolate.splev(xi, tck)
        plt.plot(xi, fx)
        plt.scatter(x, y)
    plt.show()