""" Кинотеатр
В кинотеатре n рядов по m мест в каждом. В двумерном массиве хранится информация о проданных билетах,
число 1 означает, что билет на данное место уже продано, число 0 означает, что место свободно. Поступил
запрос на продажу k билетов на соседние места в одном ряду. Определите, можно ли выполнить такой запрос.
Программа получает на вход числа n и m. Далее идет n строк, содержащих m чисел (0 или 1), разделенных
пробелами. Затем дано число k.
Программа должна вывести номер ряда, в котором есть k подряд идущих свободных мест. Если таких
рядов несколько, то выведите номер наименьшего подходящего ряда. Если подходящего ряда нет, выведите число 0.

Ввод
3 4
0 1 0 1
1 0 0 1
1 1 1 1
2

3 3
0 1 0
1 0 0
1 1 1
3

Вывод
2
0
"""

def free_place(list_, k):
    k0 = 0
    for i in range(len(list_)):
        for j in range(len(list_[i])):
            if list_[i][j] == 0:
                k0 += 1
                if k0 >= k:
                    k0 = i + 1
                    return  k0
            else:
                k0 = 0

n, m = map(int, input().split())
cinema  = list([[int(dig) for dig in input().split()] for i in range(n)])
k = int(input())

if free_place(cinema, k) == None:
    print(0)
else:
    print(free_place(cinema, k))

""" Транспонировать квадратную матрицу
Дан двумерный массив размером n×n. Транспонируйте его и результат запишите в этот же масссив.
Вспомогательный массив использовать нельзя. Решение оформите в виде функции Transpose (A)


Ввод	Вывод
3
1 2 3
4 5 6
7 8 9

Вывод
1 4 7
2 5 8
3 6 9

"""
def transpose_square_matrix(array):
    for i in range(len(array)):
        for j in range(i, len(array[i])):
            array[i][j], array[j][i] = array[j][i], array[i][j]
    return array


n = int(input())
m = [[int(num) for num in input().split()] for i in range(n)]

m = transpose_square_matrix(m)
for row in range(n):
    print(*m[row], end= ' ')
    print()
