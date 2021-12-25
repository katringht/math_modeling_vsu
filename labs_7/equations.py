import numpy as np

# Фунция с параметрами
def fun(a, b, x):
    return a * (b + x) - x ** 2


def phi(a, b, x):
    return (a * (b + x) - x ** 2 ) * (-1 / (a - x)) + x


def derivative_fun(a, x):
    return a - x


def derivative_phi(a, x):
    return (a - x) * x + 1
