# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# list_input = [1, 2, 3, 4, 5, 6, 78, 9, 34, 23, 2, 2, 3, 4, 5, 6]
# set_input = set(list_input)
# print(len(set_input))

from random import randint

list_ = []
for i in range(10):
    list_.append(randint(0,4))
print(list_)
print(len(set(list_)))

count = 0

list_1 = [list_[0]]
count = 1
for item_ in list_:
    bool_= False
    for item_1 in list_1:
        if item_ == item_1:
            bool_ = True
    if not(bool_) :
        list_1.append(item_)
        count = count + 1

print(count)
print(list_1)

list_1 = []
for i in list_:
    if i not in list_1:
        list_1.append(i)
print(len(list_1))