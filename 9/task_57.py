# Задача №57. Решение в группах
# 1. Прочесть с помощью pandas файл
# california_housing_test.csv, который находится в папке
# sample_data
# 2. Посмотреть сколько в нем строк и столбцов
# 3. Определить какой тип данных имеют столбцы
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# file='california_housing_train.csv'
# df = pd.read_csv(file)
# # print(df.head(10))
# # print(df.tail())
# # print(df.shape)
# print(df.dtypes)
# print(df.isnull().sum())
# print(df.loc[df.median_income < 2, ['median_income','median_house_value']])
# df2=(df[['longitude', 'latitude']])
# print(df.iloc[:, 0:2])
# print('-' * 35)
# print(df2.shape)
# print(df2.head())
# df2.to_excel('file_1.xlsx')
# df2.to_csv('df2.csv')
# print(df.loc[(df.housing_median_age < 20) & (df.median_house_value > 70000),
# ['housing_median_age','median_house_value']])
# print(df.median_house_value.max())
# print(df[['median_house_value']].max())
# print(df[['median_house_value']].min())
# print(df[['median_house_value']].mean())
# print(df[['median_house_value']].median())
# print(df.loc[df.median_income == 3.1250, ['median_house_value']].max())
# print(df.loc[df.median_house_value == df.median_house_value.min(), ['median_house_value', 'population']])
#df.loc[df.median_house_value == df.median_house_value.quantile(0.15)]
#print(df.median_house_value.quantile(0.05))
# df2=(df.loc[df.median_house_value < df.median_house_value.quantile(0.35), ['median_house_value', 'population']])
# print(df2.population.max())

# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке
# sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)
# df2=df.loc[df.population < 500, ['population','median_house_value']]
# print(df2.median_house_value.mean())
#
# # Задача 42: Узнать какая максимальная households в зоне минимального значения population
# print(df.population.quantile(0.15))
# df3=(df.loc[df.population < df.population.quantile(0.15), ['population', 'households']])
# print(df3.households.min())
# sns.scatterplot(data=df, x='population', y='households')
# sns.relplot(x='longitude', y='median_house_value', kind='line', data=df)
# sns.histplot(data=df, x='housing_median_age')
# plt.show()
# def add_contact():
#     file_name='phone.txt'
#     data = 'Сидоров, Иван, Петрович, 12341234'
#     with open(file_name, 'w', encoding='utf-8') as fd:
#         fd.write(data)
#
#
# def read_file():
#     file_name='phone.txt'
#     new_file = 'new_phone.txt'
#     try:
#         with open(file_name, 'r', encoding='utf-8') as fd:
#             data = fd.readlines()
#             # print(data)
#             for idx, val in enumerate(data):
#                # print(f'{idx = } {val = }')
#                print(f'{idx}) {val.rstrip()}')
#             ind_str=input('Введите необходимый номер: ')
#             try:
#                 ind=int(ind_str)
#                 print(f'{data[ind]}\n')
#                 with open(new_file, 'w', encoding='utf-8') as fd:
#                     fd.write(f'{data[ind]}\n')
#             except IndexError:
#                 print('Введено некорректное значение')
#             except ValueError:
#                 print('Введено некорректное значение')
#     except FileNotFoundError as err:
#         print('Файл еще не создан, введите данные', err)
#
# read_file()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random
lst = ['robot'] * 10
# print(lst)
lst += ['human'] * 10
# print(lst)
random.shuffle(lst)
# print(lst)

data = pd.DataFrame({'whoAmI': lst})
print(pd.get_dummies(data))
data['human'] = data['whoAmI'] == 'human'
data['robot'] = data['whoAmI'] == 'robot'
del data['whoAmI']
print(data.head(20))

