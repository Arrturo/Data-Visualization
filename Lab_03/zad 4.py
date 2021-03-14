def trojkat(a, b, c):
    if(a > b > c):
        if(a**2 == b**2 + c**2):
            print("Jest prostokątny")
    elif(b > a > c):
        if(b**2 == a**2 + c**2):
            print("Jest prostokątny")
    elif(c > a > b):
        if(c**2 == a**2 + b**2):
            print("Jest prostokątny")
    else:
        print("Nie jest prostokątny")

