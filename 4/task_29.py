# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.
import random
import sys

input_list = [random.randint(0,10) for _ in range(10)]
#input_list.insert(0,0)

print(input_list)
max = input_list[0]
if max != 0:
    i = 1
    while i < 10 and input_list[i] > 0:
        if max < input_list[i]:
            max = input_list[i]
        i += 1
    print(max)

n = int(input('Введите число '))
max_number = 0
while n != 0:
    n = int(input('Введите число '))
    if max_number < n:
        max_number = n
print(max_number)

import time
start = time.perf_counter()
#res_=[i*2 for i in range(10000000)]
res_2=(i*2 for i in range(10))
#res = []
#for i in range(10000000):
#    res.append(i * 2)
#print(res)
stop = time.perf_counter()
#print((stop - start))
#print(sys.getsizeof(res))
#print(sys.getsizeof(res_))
print(sys.getsizeof(res_2))
#print(res_2)
print('next: ', next(res_2))
print('next: ', next(res_2))
print('next: ', next(res_2))
for j in res_2:
    print(j)
