
# Задача №41. Общее обсуждение
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел


def input_array(number):
    out_list = []
    for i in range(number):
        out_list.append(int(input('Введите элемент массива: ')))
    return out_list

def func(array):
    count = 0
    for i in range(1, len(array)-1):
        if array[i-1] < array[i] and array[i] > array[i+1]:
            count += 1
    return count
N = int(input('Введите количество элементов массива: '))

print(func(input_array(N)))