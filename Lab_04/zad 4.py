class nazakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed
    def wyswietl_produkt(self):
        return self.nazwa_produktu + ' ' + str(self.cena_jed) + ' zł/' + self.jednostka_miary
    def ile_produktu(self):
        return str(self.ilosc) + self.jednostka_miary
    def ile_kosztuje(self):
        return str(self.ilosc * self.cena_jed) + ' zł'

produkt1 = nazakupy("Chleb", 5, "kg", 2)
print(produkt1.wyswietl_produkt())
print(produkt1.ile_produktu())
print(produkt1.ile_kosztuje())