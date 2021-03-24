with open("text.txt", "w+") as tekst:
    tekst.write("""Donec bibendum nisl nec nibh scelerisque, nec tempus justo feugiat. Cras lobortis sollicitudin condimentum. Cras et vulputate libero,
                    sit amet vehicula metus. Aliquam pretium ante nulla, vitae sagittis urna faucibus ac. Donec nulla enim, maximus finibus lacus vel, eleifend pharetra mi.
                    Nulla pretium sollicitudin bibendum. Sed neque lacus, lobortis scelerisque mi non, convallis euismod justo.""")

with open("text.txt", "r") as b:
    a = b.readlines()
    print(a, end = "")