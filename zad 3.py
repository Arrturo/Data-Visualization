a = int(input())
c = input()
b = int(input())

if c == 'c':
    a += b
    print(str(a))

elif c == '-':
    a -= b
    print(str(a))

elif c == '*':
    a *= b
    print(str(a))

elif c == '%':
    a %= b
    print(str(a))

elif c == '**':
    a **= b
    print(str(a))

else:
    print("Podałeś złą operację!")