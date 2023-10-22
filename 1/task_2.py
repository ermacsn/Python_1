# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

#Первый способ через string
number_str=input('Введите целое число: ')
summa = 0
for i in number_str:
    summa+=int(i)

print('Сумма цифр числа:', summa)

#Второй спрособ через int
summa=0
number_str=int(number_str)
while number_str>0 :
    summa+=number_str%10
    number_str=number_str//10

print('Сумма цифр числа:', summa)