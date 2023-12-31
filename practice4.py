import pandas as pd
import numpy as np
#1__________________________________
arr = np.array([[0, 1, 20],
                [1, 2 ,3],
                [5 ,2, 3]])
df = pd.DataFrame(arr)
print(df)
#2__________________________________
df = pd.DataFrame({'товар': [], 'цена': [],"качество":[]})
print(df)
#3__________________________________
df = pd.DataFrame({'Регион': ['Волгоградская область','Краснодарский край','Москва','Алтайский край','Камчатский край', 'Санкт-Петербург'], 'По экономике региона':[19,16.5,39.0,12.3,35.1,27.3],"Учителей, 2015":[16.8,18.3,17.1,19.0,20.1,17.5],"Учителей, 2016": [15.8,16.3,19.4,19.2,20.1,18.1]})
print(df)
print(df['Учителей, 2015'].mean())
#4__________________________________
df = pd.DataFrame({'ФИО': ['Даргский','Делябин','Лебедева','Пушкин','Светлов', 'Семенов'], 'ставка':[52000,38000,23000,80000,30000,45000],"Год рождения":[1986,1975,1999,1974,2001,1990],"Дата рождения": ['23 янв','1 май','10 июл','27 сен',"3 май","21 авг"],"Город":["Москва","Н.Новгород","Москва","Москва","Москва","Млсква"]})
print(df)
print(df[df["ФИО"] == "Светлов"])
#5__________________________________
df = pd.DataFrame({'Дерево': ['яблоня','Груша','Вишня','Яблоня','Груша','Яблоня'], 'Высота':[6, 4,4,5,3,3],"Возраст":[ 20,12,14,35,8 ,9 ],"Урожайность": [14,10,9 ,10,8 ,6 ],"Прибыль":[105,96 ,105,75,76 ,45 ]})
print(df)
print(df[df["Дерево"] == "Вишня"])
#6__________________________________
df = pd.DataFrame({"Дата":['03.10.2016','03.10.2016','04.10.2016','04.10.2016'],'Код товара': [102,102,101,101], 'Менеджер':['Петров','Сидоров','Иванов','Петров'],"Продажи":['63 р.','63 р.','51р.','102 р.']})
print(df)
print(df[df["Дата"] == "04.10.2016"])
#7__________________________________

df = pd.DataFrame({"марка":['Аudi','Аudi','Renault','Ford' ],'объем двигателя': [2.0,2.5,1.4,1.8], 'Год выпуска':[ 2007,2005 , 2010 , 2010 ],"пробег":[85020,68103,79433,66442],'Регистрационный номер':['Му№з8814М','Му№52103М','Му№85328М','МуМ98972М']})
print(df)
print(df[df["объем двигателя"] > 2])

#8__________________________________

_list = [i for i in range(1,101) ]

s = pd.Series(list)
print(s)
#9__________________________________
_list = [i for i in range(1,11) ]

s = pd.Series(list)
print(s[5:9])
#10__________________________________
_list = ['a','b','c','d','e','j','h']

s = pd.Series(list)
s[2] = 'n'
#11_________________________________
_list = [3, 56, 2, 78, 3, 71, 56, 12]
s = pd.Series(_list)
print(s[s > 10])
#12_________________________________
df = pd.DataFrame({'color':['blue','green','yellow','red','white'],"object":['ball','pen','pencil','paper','mug'],"price":[1.2,1.0,1.4,0.6,0.9]})
df['price'] = [3.0, 1.3, 2.2,0.8,0.11]
print(df)
#14_________________________________
df.at[1,'price'] = 1000
print(df)
#15_________________________________
df = pd.DataFrame({'Продукт':['шоколад','мармелад','Багет','Булочки','Сахарный пирог','шоколадное печенье'],"кв1":[123434,33434,23122132,3232323,221122,67654],"кв2":[4343,232324,32323,565657,3434,2323],'общий итог':[2174000,323,234565,645654,3543,23432]})
print(2174000 in df["общий итог"].unique())
#17_________________________________
df = pd.DataFrame({'Товар':['Персики','Виноград','Яблоки','Лимоны','Апельсины'],"Январь":[32,43,21,35,41],"Февраль":[32,24,45,12,33],"Март":[45,12,33,35,41]})

print(df['Март'].sum())