zakupy = {'mleko': 'litr', 'jajka': 'sztuki', 'Wędlina': 'dag', 'arbuz': 'sztuki', 'jabłka': 'sztuki'}
# for a,i in zakupy.items():
#     if i == 'sztuki':
#         print(a)

a = [n for n,i in zakupy.items() if i == 'sztuki']
print(a)

# 2 sposob
# prodSzt = [produkt for produkt in produkty.keys() if produkty[produkt] == "sztuki"]
