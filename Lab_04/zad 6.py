class robaczek:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self, ile_krokow):
        self.y += (ile_krokow * self.krok)

    def idz_w_dol(self, ile_krokow):
        self.y -= (ile_krokow * self.krok)

    def idz_w_prawo(self, ile_krokow):
        self.x += (ile_krokow * self.krok)

    def idz_w_lewo(self, ile_krokow):
        self.x -= (ile_krokow * self.krok)

    def pokaz_gdzie_jestes(self):
        return self.x, self.y

robak = robaczek(1, 3, 2)

robak.idz_w_gore(2)
print(robak.pokaz_gdzie_jestes())
robak.idz_w_lewo(9)
print(robak.pokaz_gdzie_jestes())
robak.idz_w_dol(1)
print(robak.pokaz_gdzie_jestes())
robak.idz_w_prawo(6)
print(robak.pokaz_gdzie_jestes())