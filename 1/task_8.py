# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n=int(input('Введите количество долек по горизонтали: '))
m=int(input('Введите количество долек по вертикали: '))
k=int(input('Введите количество долек который надо отломить: '))

if  (0 < k < n * m) and ((k >= n) or (k >= m)) and (k % n == 0 or k % m == 0):
    print('От плитки шоколадки можно отломить ', k, 'долек')
else:
    print('От плитки шоколадки нельзя отломить ', k, 'долек')

