import numpy as np

def get_M(a, b, f):
    val = []
    for x in np.linspace(a, b, 1000):
        val.append(f(x))

    return min(val)