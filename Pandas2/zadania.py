import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# #1
data = pd.read_excel('imiona.xlsx', header=0)

grupa = data.groupby(['Rok']).agg({'Liczba': ['sum']})
print(grupa)

wykres = grupa.plot()
plt.title('Liczba urodzonych dzieci w skali roku')
wykres.set_xlabel('Rok')
wykres.set_ylabel('liczba dzieci')

wykres.legend()
wykres.plot()
plt.show()

##2

data = pd.read_excel('imiona.xlsx', header=0)

grupa = data.groupby(['Plec']).agg({'Liczba': ['sum']})
print(grupa)

wykres = grupa.plot.bar()
wykres.set_ylabel('Mln')
plt.xticks(rotation=0)
wykres.plot()
plt.show()

##3

data = pd.read_excel('imiona.xlsx', header=0)

grupa = data.groupby(['Plec']).agg({'Liczba': ['sum']})

przedzial = pd.date_range(start='2012', end='2017')

wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6), legend=(0, 0))

print(wykres)
plt.legend()
plt.show()
