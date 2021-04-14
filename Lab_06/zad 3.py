import numpy as np

def funkcja(n):
    a = [2**x for x in range(1, (n*n)+1)]
    tablica = np.array(a)
    return tablica.reshape((n, n))

print(funkcja(3))