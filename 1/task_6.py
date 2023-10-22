# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

number=input('Введите шестизначное число: ')

if 5 < len(number) < 7:
    first_part = number[:3]
    second_part = number[3:]
    first_summa = 0
    for i in first_part:
        first_summa+=int(i)
    second_summa = 0
    for i in second_part:
        second_summa+=int(i)
    if first_summa == second_summa:
        print(first_part, second_part)
        print('Билетик счастливый')
else:
    print('Введеное число не является шестизначным')