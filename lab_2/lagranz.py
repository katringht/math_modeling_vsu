import matplotlib.pyplot as plt
import numpy as np
from parser_points import parser

def lagranz(x, y, t):
    z=0
    for j in range(len(y)):
        p1=1
        p2=1
        for i in range(len(x)):
            if i==j:
                p1=p1*1
                p2=p2*1   
            else: 
                p1=p1*(t-x[i])
                p2=p2*(x[j]-x[i])
        z=z+y[j]*p1/p2
    return z

def show_lagranz(i, i2):
    list_of_points = parser()
    for points in list_of_points[i:i2]:
        x = np.array(points[0], dtype=float)
        y = np.array(points[1], dtype=float)
        xnew = np.linspace(np.min(x),np.max(x),100)
        ynew = [lagranz(x,y,i) for i in xnew]
        plt.plot(x,y,'o',xnew,ynew)
        plt.grid(True)

    plt.show()
