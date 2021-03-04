""" Шахматная доска
Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*"
в шахматном порядке. В левом верхнем углу должна стоять точка.

"""

'''Variant 1'''

n = 8
m = 8
a = []
for i in range(n):
    a.append([0]*m)
    for j, elem in enumerate(a[i]):
        if (i + j)%2 == 0:
            elem = ' '
        else:
            elem = '*'
        print(elem.center(3, ' '), end='')
    print()

'''Variant 2'''

n_cell = 8
chess_board = [ [' ' for j in range(n_cell)] for i in range(n_cell)]

steam_cell = False
for line in chess_board:
    for cell in line:
        if steam_cell:
            cell = '[_]'
        steam_cell = not steam_cell
        print(cell.center(3, ' '), end='')
    if n_cell % 2 != 1:
        steam_cell = not steam_cell
    print()

''' Заполнение в шахматном порядке
Даны числа n и m. Заполните массив размером n×m в шахматном порядке:
клетки одного цвета заполнены нулями, а другого цвета - заполнены числами натурального
ряда сверху вниз, слева направо. В левом верхнем углу записано число 1.
Выведите полученный массив на экран, отводя на вывод каждого элемента ровно 4 символа.'''

n, m = map(int, input().split())
b = [[(i + j + 1)%2 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        b[i][j] = str(b[i][j]).rjust(2, ' ')
        print(b[i][j], end=' ')
    print()