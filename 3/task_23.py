# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

from random import randint

n = 10
k = 3
list_ = []
for i in range(n):
    list_.append(randint(0,k))
print(list_)
count = 0
for i in range(len(list_) - 1):
    if list_[i] < list_[i + 1]:
        count += 1
print(count)

count = 0
for i in range(1, len(list_)):
    if list_[i-1] < list_[i]:
        count += 1
print(count)