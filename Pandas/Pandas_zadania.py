import numpy as np
import pandas as pd
from pandas.core import groupby
import xlrd
import openpyxl

##1
df = pd.read_excel('imiona.xlsx')
# print(df)

##2
# print(df[df['Liczba'] < 1000])

# print(df[df["Imie"] == "Artur"]

# print(df["Liczba"].sum())

# df_4 = df[(df["Rok"] >= 2005) & (df["Rok"] <= 2010)]
# print(df_4["Rok"].sum())




##3
# df = pd.read_csv('zamowienia.csv', header=0, sep=';')
# print(df)

