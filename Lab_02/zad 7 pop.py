liczby = [1, 2, 3, 4, 5, 5.5]
for i in range(0, len(liczby), 1):
    if i == 0:
        print(liczby[i])
    else:
        suma = liczby[i] + liczby[i-1]
        print(suma)