from spline import *
from lagranz import *
from piecewise_linear import *
from parabolic import *
from parser_points import *

def get_charts():
    i, i1 = choose_charts(len(curLen))
    print("Choose one of the interpolation methods:\n1 - Lagranz\n2 - piecewise linear\n3 - parabolic\n4 - spline")
    request = str(input("Enter a value: "))
    if request == '1':
        show_lagranz(i,i1)
    elif request == '2':
        show_piecewise_linear(i,i1)
    elif request == '3':
        show_piecewise_parabolic_charts(i, i1)
    elif request == '4':
        spline(i,i1)
    else:
        print("Invalid command")

curLen = parser()    
get_charts()
