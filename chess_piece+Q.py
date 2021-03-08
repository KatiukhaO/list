""" Ходы коня
На шахматной доске стоит конь. Отметьте положение коня на доске и все клетки, которые бьет конь.
Программа получает на вход координаты коня на шахматной доске в шахматной нотации
(то есть в виде “e4”, где сначала записывается номер столбца (буква от “a” до “h”, слева направо),
затем номеру строки (цифра от 1 до 8, снизу вверх).
Клетку, где стоит конь, отметьте буквой “K”, клетки, которые бьет конь, отметьте символами “*”, 
остальные клетки заполните точками.
Выведите на экран изображение доски.

Ввод	
b6

Вывод
* . * . . . . .
. . . * . . . .
. K . . . . . .
. . . * . . . .
* . * . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .

"""
posision = input()
x = posision[0]
y = int(posision[-1]) - 1
coordinat = {'a': 0,
             'b': 1,
             'c': 2,
             'd': 3,
             'e': 4,
             'f': 5,
             'g': 6,
             'h': 7}

for key in coordinat:
    if key == x:
        x = coordinat[key]

chess_board = [['.'] * 8 for i in range(8)]
for i in range(len(chess_board)):
    for j in range(len(chess_board[i])):
        if abs(y - i) + abs(x - j) == 0:
            chess_board[i][j] = '♘'
        elif abs((x - j) * (y - i)) == 2:
            chess_board[i][j] = '*'

for row in reversed(chess_board):
    print(' '.join(row))
print('___________________________________________________________________')

"""Решите предыдущую задачу для ферзя. Ферзь обозначается буквой “Q” """

chess_board = [['  ']*8 for i in range(8)]
for i in range(len(chess_board)):
    for j in range(len(chess_board[i])):
        if y == i and x == j:
            chess_board[i][j] = 'Q'
        elif (i != y or j != x) and (i == y or j == x) or (abs(i - y) == abs(j - x)):
            chess_board[i][j] = '*'

color = True
for row in reversed(chess_board):
    for cell in row:
        if color == False:
            print('\033[46m', cell.ljust(2, ' '), end='')
            color = not color
        else:
            print('\033[44m', cell.ljust(2,' '), end='')
            color = not color
    print('\033[0m')
    color = not color
