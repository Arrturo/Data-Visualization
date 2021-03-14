z = 0
parzyste = []
while z != 10:
    liczba = input("Wpisz liczbę: ")
    liczba = float(liczba)
    if liczba % 2 == 0:
        parzyste.append(liczba)
    z += 1
print(parzyste) 