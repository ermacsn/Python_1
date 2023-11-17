# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

list_input = [1, 3, 3, 3, 5]
#
# def reverse (list_):
#     max_ = min_ = n = m = 0
#     for i in range(len(list_input)):
#         if max_ < list_[i]:
#             max_ = list_[i]
#             n = i
#         if min_ > list_[i]:
#             min_ = list_[i]
#             m = i
#     print(n, m)
#     list_[n] = list_[m]
#     return list_
#
# print(reverse(list_input))
import time
start1 = time.time_ns()
print([min(list_input) if i == max(list_input) else i for i in list_input])
print(time.time_ns() - start1)

start2 = time.time_ns()
def grades_correction(array, i, max_num):
    if i == -1:
        return
    if array[i] == max_num:
        array[i] = min(array)
    return grades_correction(array, i - 1, max_num)


grades_correction(list_input, len(list_input) - 1, max(list_input))
print(time.time_ns() - start2)
#print(*list_input)

