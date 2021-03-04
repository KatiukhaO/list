'''Напишите программу, которая запрашивает с ввода восемь чисел, добавляет их в список. На
экран выводит их сумму, максимальное и минимальное из них. Для нахождения суммы,
максимума и минимума воспользуйтесь встроенными в Python функциями sum(), max() и min().'''

b = list()
for i in range(8):
    a = float(input('iNPUT numeric : '))
    b.append(a)
print(b)
print(sum(b),max(b), min(b))

s = [float(input('iNPUT numeric : ')) for i in range(8)]
print(s)
print(sum(s), min(s), max(s))

'''Напишите программу, которая генерирует сто случайных вещественных чисел и заполняет
ими список. Выводит получившийся список на экран по десять элементов в ряд. Далее
сортирует список с помощью метода sort() и снова выводит его на экран по десять элементов
в строке. Для вывода списка напишите отдельную функцию, в качестве аргумента она
должна принимать список.'''

from random import random, randint
from math import

def print_list(array, len_part = 10):
    i = 0
    while i < ceil(len(array)/len_part):
        print(array[i*len_part : i*len_part + len_part])
        i += 1

def print_listW(array):
    i = 0
    while i < 100/10:
        j = 0
        while j < 10:
            print(array[j + i], end=' ')
            j += 1
        print()
        i += 1

start = float(input('Input renge random numerik : '))
stop = float(input('Input renge random numerik : '))
n = int(input('Len List :'))
a = [round(random()*(stop - start) + start, 2) for x in range(n)]

print_listW(a)

a = sorted(a)
print_list(a, 10)





