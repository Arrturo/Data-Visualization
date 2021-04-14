import numpy as np

def funkcja(d):
    macierz = np.diag([x for x in range(d, 0, -1)], 2)
    return macierz

print(funkcja(8))