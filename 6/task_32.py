# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

list_ = [0, 4, 7, 5, 8, 10, 5, 3, 8]
max_ = 9
min_ = 3
index_ = []

for i in range(len(list_)):
    if list_[i] >= min_ and list_[i] <= max_:
        index_.append(i)

print(index_)