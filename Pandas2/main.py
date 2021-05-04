import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# #korzystając z funkcji random oraz data_range możemy
# #wygenerować szereg czasowy danych
#
# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2015', periods=1000))
#
# #funkcja biblioteki pandas generująca skumulowaną sumę
# #kolejnych elementów
#
# ts = ts.cumsum()
# print(ts)
# ts.plot()
# plt.show()

# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'], 'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
#         'Populacja': [11190846, 13031710, 207847528, 38675467]}
#
# df = pd.DataFrame(data)
# print(df)
#
# grupa = df.groupby(['Kontynent']).agg({'Populacja': ['sum']})
# print(grupa)
#
# wykres = grupa.plot.bar()
# wykres.set_xlabel('Kontynent')
# wykres.set_ylabel('Mld')
# wykres.legend()
#
# plt.xticks(rotation=0)
# plt.savefig('Wykres.png')
# plt.title('Populacja z podziałem na kontynenty')
# plt.show()


# df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
# print(df)
#
# grupa = df.groupby(['Imię i nazwisko']).agg({'Wartość zamówienia': ['sum']})
# print(grupa)
# wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6), legend=(0, 0))
# plt.legend(loc='lower right')
# plt.title('Suma zamówienia dla sprzedawcy')
# plt.show()

# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2015', periods=1000))
#
# ts = ts.cumsum()
#
# df = pd.DataFrame(ts)
#
# df['MA'] = df.rolling(window=100).mean()
# df.plot()
# plt.show()


# plt.plot([1, 2, 3, 4])
# plt.ylabel('Jakieś liczby')
# plt.show()


# plt.plot([1, 2, 3, 4], [1, 4, 8, 16], 'ro-')
# plt.axis([0, 6, 0, 20])


# plt.plots([1, 2, 3, 4], [1, 4, 8, 16], 'r')
# plt.plots([1, 2, 3, 4], [1, 4, 8, 16], 'o')
#
# plt.axis([0, 6, 0, 20])
# plt.show()

##pierwsza metoda
# t = np.arange(0., 5., 0.2)
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()

#druga metoda
# x = np.linspace(0, 2, 100)
# plt.plot(x, x, label='postać liniowa')
# plt.plot(x, x**2, label='postać kwadratowa')
# plt.plot(x, x**3, label='postać sześcienna')

# plt.xlabel('etykieta x')
# plt.ylabel('etykieta y')

# plt.title('Prosty wykres')
# plt.legend()

# plt.show()

# #wykres f. sinus
# x = np.arange(0, 10, 0.1)
# s = np.sin(x)
# plt.plot(x, s, label='sin(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('sinusoida')
# plt.legend()
# plt.show()

# x1 = np.arange(0.0, 2.0, 0.02)
# x2 = np.arange(0.0, 2.0, 0.02)

# y1 = np.sin(2 * np.pi * x1)
# y2 = np.cos(2 * np.pi * x1)

# plt.subplot(2, 1, 1)
# plt.plot(x1, y2, '-')
# plt.title('Dwa podwykresy')
# plt.ylabel('sin(x)')

# plt.subplot(2, 1, 2)
# plt.plot(x2, y2, 'r-')
# plt.xlabel('cos(x)')

# plt.show()
