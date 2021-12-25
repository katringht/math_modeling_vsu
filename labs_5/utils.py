import random
import numpy as np

def random_v(N):
    r = []
    for _ in range(N):
        r.append(random.random())
    return r

def get_M(a, b, f):
    val = []
    for x in np.linspace(a, b, 1000):
        val.append(f(x))

    return max(val), min(val)