# a = []
# for x in range(1, 11):
#     a.append(1-x)
# print(a)

# b = []
# for x1 in range(5):
#     b.append(4**x1)
# print(b)

# c = []
# for x2 in b:
#     if x2 %2 == 0:
#         c.append(x2)
# print(c)

a = [1-x for x in range(1, 11)]
b = [4**x1 for x1 in range(5)]
c = [x2 for x2 in b if x2 %2 == 0]

print(a, b, c)