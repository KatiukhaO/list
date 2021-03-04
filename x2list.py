''' Таблица умножения
Даны числа n и m. Создайте двумерый массив размером n×m и заполните его таблицей
умножения по формуле A[i][j] = i * j. При заполнении массива нельзя использовать вложенные циклы.
Выведите получившийся массив на экран (при выводе можно использовать вложенные циклы),
отводя на вывод каждого числа ровно 4 символа.'''

n, m = map(int, input('Input n , m : ').split())
a = [[i*j for j in range(m)] for i in range(n)]  

for row in a:
    for elem in row:
        elem = str(elem).rjust(4, ' ')
        print(elem, end=' ')
    print()

''' щоб вивести числа попорядку замість i*j треба записати вираз i*m+j'''

''' Симметричен ли массив?
Дано число n и массив размером n×n. Проверьте, является ли этот массив симметричным 
относительно главной диагонали. Выведите слово “YES”, если массив симметричный, 
и слово “NO” в противном случае.
Решение оформите в виде функции IsSymmetric(A).'''

def IsSymmetric(array):
    flag = True
    for i in range(len(array)):
        for j in range(i):
            if array[i][j] != array[j][i]:
                flag = False
    return flag

n = int(input())
A = []
for i in range(n):
    A.append(list(map(int, input().split())))

if IsSymmetric(A):
    print('Yes')
else:
    print('No')