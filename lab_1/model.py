import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import parser

def parser():
    f = open("points.txt", "r")
    list_of_points = []
    for line in f:
        val = [map(float,(s.split(","))) for s in line.split(";")]
        list_of_points.append(val)
    return list_of_points


def show_chart(i, i2):
    list_of_points = parser()
    colors = iter(cm.rainbow(np.linspace(0, 1, len(list_of_points))))
    for points in list_of_points[i:i2]:
        x = points[0]
        y = points[1]
        plt.scatter(x, y, color=next(colors))

    plt.show()


def get_charts(currentLen):
    print("Number of charts - {}.\nAccessible commands:\n'0' - all charts\n couple of numbers'12' - first and second charts\n '3' - just third chart".format(currentLen) )
    request = str(input("Enter a value: "))
    if len(request) == 1:
        if int(request) == 0:
            show_chart(0, len(curLen))
        else:
            show_chart(int(request) - 1, int(request))
    elif len(request) == 2:
        if int(request[0]) < int(request[1]):
            show_chart(int(request[0]) - 1, int(request[1]))
        else: show_chart(int(request[1]) - 1, int(request[0]))
    else: 
        print("Incorrect input")


curLen = parser()
get_charts(len(curLen))
