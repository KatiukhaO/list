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
