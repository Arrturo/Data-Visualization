a = float(input("Podaj pierwszą liczbę: "))
c = input("Podaj znak: ")
b = float(input("Podaj drugą liczbę: "))


if c == '+':
    print("wynik: " + str(a + b))
elif c == '-':
    print("wynik: " + str(a - b))

elif c == '*':
    print("Wynik: " + str(a * b))

elif c == '/':
    try:
        print("wynik: " + str(a / b))

    except ZeroDivisionError:
        print("Nie można dzielić przez 0!")

elif c == '^':
    print("Wynik: " + str(a ** b))

else:
    print("Wprowadziłeś zły operator.")
