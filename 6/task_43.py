# адача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках
import random


def input_array(number):
    out_list = []
    for i in range(number):
        out_list.append(int(input('Введите элемент массива: ')))
    return out_list

# def func_para(array):
#     if len(array) < 2:
#         return
#     count = 0
#     for i in array:
#         if i in array:
#             array.remove(i)
#             array.remove(i)
#             count += 1
#     return count
def func_set(array: list):
    array_set = set(array)
    print(*array_set)
    gl_count = 0
    for item in array_set:
        count = 0
#        for i in range(len(array)):
#            if item == array[i]:
#                count += 1
        count = array.count(item)
        print(count)
        gl_count += count // 2
    return gl_count

def create_random_list(num):
    return [random.randint(-10, 10) for _ in range(num)]

N = int(input('Введите количество элементов массива: '))

#arr1 = input_array(N)
arr2 = create_random_list(N)
print(*arr2)
# print(func_para(arr1))
print(func_set(arr2))