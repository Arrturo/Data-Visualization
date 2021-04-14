import numpy as np

def funkcja(n, m):
    return np.logspace(1, m, m, True, n, int)

print(funkcja(2, 4))