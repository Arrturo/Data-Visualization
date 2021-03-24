import random
lista = []
plik = open("plik.txt", "w+")
for i in range(0, 30):
    a = random.randint(0, 30)
    a *= 2
    lista.append(a)
plik.write(str(lista))
plik.close()
