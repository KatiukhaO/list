
n, m = map(int, input('Input size chess board : ').split())
chess_board = [['*' for j in range(m) if (i + j)%2 != 0] for i in range(n)]
for line in chess_board:
    for cell in line:
        print(cell, end=' ')
    print()