# Задача №37.
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

number = int(input('Enter numnber: '))
def sort_function(number):
    if number == 0:
        return
    x = input('Enter: ')
    sort_function(number - 1)
    print(x)

sort_function(number)

def reverse_output(n, x = None):
    if n > 0:
        x = input('Enter number: ')
        reverse_output(n - 1)
    print(x, end=" ")

reverse_output(number)

def rec(n):
    if n == 0:
        return ''
    return f'{rec(n - 1)} {input("Enter number: ")}'

print(rec(number))