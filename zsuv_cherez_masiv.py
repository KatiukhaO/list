val_element_list = int(input('Введіть значення, кількості елементів списку : '))
a = list(range(1,val_element_list+1))
print('a : ', a)
left_right = input('Введіть напрямок зсуву (<вліво/вправо>) : ')
k = int(input('Введіть значення, кількості елементів зсуву : '))
n = int(len(a))
b = [0]*k

if left_right.lower() == 'right' or left_right.lower() == 'вправо' or left_right.lower() == 'праворуч':
    i = 0
    while i < k:
        b[i] = a[n - k + i]
        i += 1

    i = 0
    p = n - 1
    while i < n - k:
        a[p - i] = a[p - k -i]
        i += 1

    i = 0
    while i < k:
        a[i] = b[i]
        i += 1
    print('a : ', a)

elif left_right.lower() == 'left' or left_right.lower() == 'вліво' or left_right.lower() == 'ліворуч':
    i = 0
    while i < k:
        b[i] = a[i]
        i += 1

    i = 0
    while i < n - k :
        a[i] = a[k + i]
        i += 1

    i = 0
    while i < k:
        a[n - k + i] = b[i]
        i += 1

    print('a : ', a)
else:
    print('Введіть коректний напрямок!')