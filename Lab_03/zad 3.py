zakupy = {'mleko': 'litr', 'jajka': 'sztuki', 'Wędlina': 'dag', 'arbuz': 'sztuki', 'jabłka': 'sztuki'}
# for a,i in zakupy.items():
#     if i == 'sztuki':
#         print(a)

a = [n for n,i in zakupy.items() if i == 'sztuki']
print(a)