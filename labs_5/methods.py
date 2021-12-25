from utils import *
from random import random


def trapezoid_rule(func, a, b, N):
    """Правило трапеций
       N - число отрезков, на которые разбивается [a;b]"""
    h = (b - a) / N # высота 
    sum = 0.5 * (func(a) + func(b))
    for i in range(1, N):
        sum += func(a + i * h)
# площадь трапеции 
    return sum * h 

# monte carlo
#  1 способ 
def monte_carlo_1_method(f, a, b, N):
    s = 0
    r = random_v(N)
    for i in range(N):
        U = r[i] * (b - a) + a
        s += f(U)
    I = (b - a) / N * s
    return I

#  2 способ
def monte_carlo_Second_mathod(f, a, b, N):
    k = 0
    max, minim = get_M(a, b, f)
    X = a + (b - a) * random()
    Y =  minim * (max - minim) * random()
    for i in range(N):
        if Y < f(X):
            k += 1

    I = (max - minim) * (b - a) * (k / N)
    return I


