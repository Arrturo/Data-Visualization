a = [1, 2, 3, 4, 5, 6]

for i in a:
    if (i == 1) | (i == 6):
        print('O' * 6)
    else:
        print('O' + ' ' * 4 + 'O')
