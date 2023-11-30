# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая
# состоит всего из 1 столбца. Ваша задача перевести его в one hot вид.
# Сможете ли вы это сделать без get_dummies?
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(pd.get_dummies(data)) # для проверки
data['human'] = data['whoAmI'] == 'human' #добавляем столбцы
data['robot'] = data['whoAmI'] == 'robot'
del data['whoAmI'] #удаляем первый столбец
print(data.head(20))

