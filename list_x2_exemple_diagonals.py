""" Диагонали параллельные главной
 Дано число n. Создайте массив размером n×n и заполните его по следующему правилу.
На главной диагонали должны быть записаны числа 0. На двух диагоналях, прилегающих
к главной, числа 1. На следующих двух диагоналях числа 2, и т.д.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

n = int(input('Input size square, n : '))


matrix = [[abs(j - i) for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()


""" Побочная диагональ
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:
Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.
Числа, стоящие выше этой диагонали, равны 0.
Числа, стоящие ниже этой диагонали, равны 2.
Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.
"""

m = int(input('Input m - size matrix m x m : '))

a = []
for i in range(m):
    a.append([0]*m)
    for j in range(m - i, m):
        a[i][j] = 2
        a[i][m - 1 - i] = 1
    print(' '.join(map(str, a[i])), end=' ')
    print()

""" Поменять столбцы
Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.
Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.
Решение оформите в виде функции SwapColumns (A, i, j).

Ввод	Вывод
3 4
11 12 13 14
21 22 23 24
31 32 33 34
0 1

Вывод
12 11 13 14
22 21 23 24
32 31 33 34

"""

def change_column(list, number_column_first, number_column_second):
    for line in list:
        line[number_column_first], line[number_column_second] = line[number_column_second], line[number_column_first]
    return list


n, m = map(int, input('Input n, m :').split())
i, j = map(int, input('Input i, j :').split())

list_ = [list(map(int, input().split())) for i in range(n)]

list_ = change_column(list_, i, j)
for line in list_:
    print(' '.join(map(str, line)), end=' ')
    print()




