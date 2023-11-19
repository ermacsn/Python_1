#
# list_ = [1, 2, 3, 5, 8, 15, 23, 38]
#
# def math(op, list_loc):
#     list_ret = []
#     for x in list_loc:
#         if op(x) :
#             list_ret.append((x, x**2))
#     return list_ret
#
# print(math(lambda a: a%2 == 0, list_))
#
# def select(f, col):
#     return [f(x) for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]
#
# res = select(int, list_)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
#
# print(select(lambda x: (x, x**2), res))
#
# list_1 = [x for x in range(1, 20)]
# print(list_1)
#
# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

# data = [15, 20, 35, 45, 57, 63, 75, 85, 95, 9]
# # print(data)
# # data = list(map(int, data.split()))
# # print(data)
# res = list(filter(lambda x: x% 10 == 5, data))
# print(res)

# users = ['user1', 'user2', 'user3', 'user4']
# ids = [4, 5, 6, 7]
# print(list(zip(users, ids)))
# salary = [11, 22, 33]
# print(list(zip(users, ids, salary)))
# print(dict(enumerate(users)))

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a', encoding='utf-8')
# data.writelines(colors)
# data.close()\

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

import os

print(os.getcwd())
os.chdir(/home/ermac_/Work/GeekBrains/Programming/Python/Practica/pythonProject)