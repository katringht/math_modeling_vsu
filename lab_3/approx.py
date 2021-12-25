import matplotlib.pyplot as plt
import numpy as np
from my_parser import *


def approx(x, y, degree):
    polinom = np.polyfit(x, y, degree, full=True)[0]
    f_polinom = np.poly1d(polinom)
    fx = np.linspace(np.min(x), np.max(x), 1000)
    plt.plot(fx, f_polinom(fx))
    plt.grid(True)


def show_chart():
    i, i1 = choose_charts(len(curLen))
    list_of_points = parser()
    print("Enter the power of the fitting polynomial")
    degree = int(input())
    for points in list_of_points[i:i1]:
        x = sorted(points[0])
        y = sorted(points[1])
        approx(x, y, degree)
        plt.scatter(x, y)
    plt.show()

curLen = parser()
show_chart()