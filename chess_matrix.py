'''Chess matrix'''
"""version3.0"""

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

    '''modifie'''