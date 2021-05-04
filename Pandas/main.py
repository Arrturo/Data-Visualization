import numpy as np
import pandas as pd
import xlrd
import openpyxl

# # series
# s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)

# s = pd.Series([10, 12, 8, 14], index=['Ala', 'Marta', 'Marek', 'Wiesiek'])
# print(s)

# # dataframe za pomoca slownika

# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
#         'Populacja': [11190864, 1303171035, 20747528]}
# df = pd.DataFrame(data)
# print(df)

# # dataframe przechowuje typ dla każdej z kolumn i możemy go sprawdzić w nastepujacy sposob
# print(df.dtypes)

# # seria danych, czyli próbki dla kolejnych dat
# daty = pd.date_range('20210324', periods=5)
# print(daty)

# df = pd.DataFrame(np.random.randn(5, 4), index=daty, columns=list('ABCD'))
# print(df)

# pandas umożliwia tworzenie dataframe z zewnetrznych źródeł np. plik csv. xcl.
df = pd.read_csv('Wyniki.csv', header=0, sep=';')
print(df)
df.to_csv('plik.csv', index=False)

# xlsx = pd.ExcelFile('Wyniki.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df)

# df.to_excel('plik.xlsx', sheet_name='arkusz pierwszy')


# # pobieranie danych ze struktur

# s = pd.Series([10, 12, 8, 14], index=['Ala', 'Marta', 'Marek', 'Wiesiek'])
# print(s)

# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
#         'Populacja': [11190864, 1303171035, 20747528]}
# df = pd.DataFrame(data)

# # #pojedyńczy element z serii odnosimy sie do nazwy indexu
# # print(s['Wiesiek'])
# print(s.Wiesiek)

# # pojedynczy element z ramki danych, tak jak przy cięciu tablic
# # tylko te ciecia sa oparte o indexy

# print(df[0:1])
# print(df['Populacja'])
# print(df.iloc[[0][0]])
# print(df.loc[[0], ['Kraj']])
# print(df.at[0, 'Kraj'])

# print('Kraj: ' + df.Kraj)

# # losowe pobieranie elementow z ramki danych lub w odniesieniu do procentowej wartosci calego zbioru

# # jeden element losowy z dataframe
# print(df.sample())

# # dwa elementy
# print(df.sample(2))

# print(df.sample(frac=0.5))
# print(df.sample(n=10, replace=True))
# print(df.head(2))
# print(df.tail(2))

# print(df.describe())
# print(df.T)

# print(s[s > 9])
# print(s.where(s > 10))
# print(s.where(s > 10, 'za duże'))

# seria = s.copy()
# seria.where(s > 10, 'za duże', inplace=True)
# print(seria)

# print(s[~(s > 10)])
# print(s[(s > 8) & (s < 13)])

# s['Wiesiek'] = 15
# print(s)
# s['Alan'] = 16
# print(s)

# print(df[df['Populacja'] > 120000000])
# print(df[((df.Populacja) > 1000000) & (df.index.isin([0, 2]))])

# szukaj = ['Belgia', 'Brasilia']
# print(df.isin(szukaj))

# df.loc[3] = 'dodana'
# print(df)

# df.loc[4] = ['Polska', 'Warszawa', 40_000_000]
# print(df)

# new_df = df.drop([3])
# print(df)

# df.drop([3], inplace=True)
# print(df)

# # grupowanie, sortowanie, funkcja agregująca

# df['Kontynent'] = ['Europa', 'Azja', 'Ameryka płd', 'Europa']
# print(df.sort_values(by='Kraj'))

# grouped = df.groupby(['Kontynent'])
# print(grouped.get_group('Europa'))

# print(df.groupby(['Kontynent']).agg({'Populacja': ['sum']}))
