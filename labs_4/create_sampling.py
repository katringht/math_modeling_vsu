#! /usr/bin/env python
# -*- coding: utf-8 -*-
from math_utils import *
import random as rnd


# Возвращаем выборку и интервал
def normal_sampling(a, b):
    if a > b:
        print("Данные некорректны")
        raise SystemExit(1)
    r = generate_random_variables(1000)
    x = []
    for i in r:
        xr = reverse_fun(i, a, b)
        x.append(xr)
    x = sorted(x)
    interval = [a, b]
    return x, interval


def create_gauss_sampling(m, d):
    sigma = math.sqrt(d)
    n = 6 # число членов суммы 
    x = []
    for _ in range(1000):
        v = 0
        for _ in range(n):
            v += rnd.random()
        xi = fun_gauss(v, m, sigma, n) # нормализированный стандартный закон гауссовского распределения 
        x.append(xi)
    x = sorted(x)
    # Интервал от минимального до максимального x
    interval = [x[0], x[-1]]
    return x, interval


def create_rayleigh_sampling(sigma, n):
    max_y = rayleigh_distribution(sigma, sigma)
    ri = generate_random_variables(3000)
    x = []
    i = 1
    while i < 3000:
        X = sigma * n * ri[i]
        Y = max_y * ri[i - 1]
        if Y <= rayleigh_distribution(X, sigma):
            x.append(X)
        i += 1
        if len(x) >= 1000:
            break
    x = sorted(x)
    # Интервал от 0 до максимального X
    interval = [0, x[-1]]
    return x, interval
