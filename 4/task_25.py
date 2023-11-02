# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

#input_ = input ('Введите строку одиночных символов через пробел: ')
input_ = 'a a a b c a a d c d a'

user_list = input_.split()
result_list = []
for i in range(len(user_list)):
    tmp = user_list[:i].count(user_list[i])
    if tmp >= 1:
        result_list.append(f'{user_list[i]}_{tmp}')
    else:
        result_list.append(user_list[i])

print(" ".join(result_list))

string_dict = dict()
zero = ""
for i in user_list:
    if i in string_dict:
        string_dict[i] += 1
        zero += f"{i}_{string_dict[i]} "
    else:
        string_dict[i] = 0
        zero += f"{i} "
print(zero)
print(string_dict)

set_ = set(input_.split())
for item in set_:
    count = 0
    i = 0
    while i <= len(input_) - 1:
        if item == input_[i]:
            if count != 0:
                input_ = input_[:i + 1] + '_' + str(count) + input_[i + 1:]
            if i == len(input_):
                input_ = input_ + '_' + str(count)
            count += 1
        i += 1
print(input_)



