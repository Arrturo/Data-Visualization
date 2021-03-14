import random

# lista1 = []
# for i in range(10):
#     n = random.randint(0,20)
#     lista1.append(n)
#     if(n %2 == 0):
#         print(n)

lista1 = []
for i in range(10):
    n = random.randint(0,20)
    lista1.append(n)
print(lista1)
a = [lista1 for lista1 in lista1 if lista1 %2 == 0]
print(a)