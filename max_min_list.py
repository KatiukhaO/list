'''Напишите программу, которая запрашивает у пользователя шесть вещественных чисел. На
экран выводит минимальное и максимальное из них, округленные до двух знаков после
запятой. Выполните задание без использования встроенных функций min() и max().'''


b = list()
for i in range(6):
    a = float(input('Input float value :'))
    b.append(a)

minimum = b[0]
maximum = b[0]
for i in b:
    if i < minimum:
        minimum = i
    elif i> maximum:
        maximum = i

print('minimum = ', minimum)
print('maximum = ', maximum)