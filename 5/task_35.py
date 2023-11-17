# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

#number = int(input('Введите число: '))
def number_of(number):
     if number == 1:
         return False
     result = True
     for i in range(2, number // 2):
 #        print(number % i)
         if number % i == 0:
             result = False
     return result

for n in range(1,100):
     if number_of(n):
         print(n)

def numbers_rec(n, i = None):
    if i is None:
        i = n // 2
    if i == 1:
        return True
    if n <= 1 or n % i == 0:
        return False
    return numbers_rec(n, i - 1)

for n in range(1,100):
     if numbers_rec(n):
         print(n)


num = int(input('Enter number: '))
res = 'None'
for i in range(2, int(num**(0.5) + 1)):
    if num % i == 0:
        res = 'complex'
        break

print(num**(0.5))
print(int(num**(0.5) ))
print(int(num**(0.5) + 1))
print(res)