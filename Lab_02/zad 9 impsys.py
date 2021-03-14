import sys as system
lista = [1, 2, 3, 4, 5, 6]
# for a in lista:
#     if(a == 1) | (a == 6):
#         for b in lista:
#             system.stdout.write("O")
#         system.stdout.write("\n")
#     else:
#         system.stdout.write("O")
#         for c in range(4):
#             system.stdout.write(" ")
#         system.stdout.write("O")
#         system.stdout.write("\n")

for a in lista:
    for b in lista:
        if(a == 1) | (a == 6):
            system.stdout.write("O")
        else:
            if(b == 1) | (b == 6):
                system.stdout.write("O")
            else:
                system.stdout.write(" ")
    system.stdout.write("\n")