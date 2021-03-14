def nty_wyraz_g(a, q, n):
    an = a * (q ** (n-1))
    return an

def sum_g(a, n, q):
    if(q != 1):
        sn = a * (1 - pow(q,n))/(1-q)
    elif(q == 1):
        sn = a * n