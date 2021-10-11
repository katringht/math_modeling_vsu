from spline import *
from lagranz import *
from piecewise_linear import *
from parabolic import *

def get_charts():
    print("Choose one of the interpolation methods:\n1 - Lagranz\n2 - piecewise linear\n3 - parabolic\n4 - spline")
    request = str(input("Enter a value: "))
    if request == '1':
        show_lagranz('points1.txt')
    elif request == '2':
        show_piecewise_linear('points2.txt')
    elif request == '3':
        show_piecewise_parabolic_charts("points3.txt")
    elif request == '4':
        spline('points4.txt')
    else:
        print("Invalid command")
    
get_charts()
