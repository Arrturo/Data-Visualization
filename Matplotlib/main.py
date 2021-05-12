import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# x1 = np.arange(0.0, 2.0, 0.02)
# x2 = np.arange(0.0, 2.0, 0.02)
# y1 = np.sin(2 * np.pi * x1)
# y2 = np.cos(2 * np.pi * x2)
#
# plt.subplot(3, 2, 1)
# plt.plot(x1, y1, '-')
# plt.title('wartosci sinusa')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
#
# plt.subplot(324)
# plt.plot(x2, y2, 'r-')
# plt.title('wartosci cosinusa')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
#
# plt.subplot(325)
# plt.plot(x1, y1, 'r-')
# plt.title('wartosci cosinusa')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
#
# plt.show()
#
#
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}

data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('wartosci a')
plt.ylabel('wartosci b')
plt.grid()
plt.show()
#
# etykiety = ['Kobiety', 'Mężczyźni']
# wartosci = [345, 435]
# rozmiar = plt.figure(figsize=(8, 10))
# plt.bar(etykiety, wartosci, figure= rozmiar)
# plt.xticks(rotation=45)
#
# plt.bar(etykiety, wartosci)
# plt.xlabel('Płeć')
# plt.ylabel('Ilość narodzin')

#histogram
# x = np.random.randn(10000)
# plt.hist(x, bins=50, facecolor='g', alpha=0.75, density=True)
#
# plt.xlabel('Wartosci')
# plt.ylabel('Prawdopodobieństwa')
# plt.title('Histogram')
#
# plt.grid()
# plt.show()

#wykres kołowy
# zawodnicy = ['Messi', 'Suarez', 'Dembele', 'Coutinho']
# bramki = [48, 25, 13, 11]

# wedges, texts, autotexts = plt.pie(bramki, labels=zawodnicy,
#                                    autopct=lambda pct:
# '{:.1f}%'.format(pct), textprops=dict(color='black', fontsize=20))
# plt.setp(autotexts, size=14, weight='bold')

# plt.title('Wykres kołowy z procentowym udziałem strzelonych bramek')
# plt.legend(title='Zawodnicy')
# plt.show()