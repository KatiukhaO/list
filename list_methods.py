array = [1,2,3,4,5,6,7,8,9,1,2,3]
print(array)

array2 = list(array)
print(array2)

print(array2[-4])
print(array[-4])
print(array2[0])
print(array2[4])

array[3] = 31
print(array)

array3 = [7] * 7
print(array3)

a = 10
array = list(range(a+1))
print(array)

array = list(range(5, a+1))
print(array)

array = list(range(a, a*10, a))
print(array)
for x in array:
    print(x)


i = 0
while i < len(array2):
    print ('array2 = ', array2[i])
    i += 1

print(len(array2))

if array == array2:
    print('Списки однакові')
else:
    print("Списки різні")

name = list()
name.append('Tomas')
name.append(array)
print(name)

name.insert(1, 'Nick') # додає елемент по індексу
print(name)

name.remove('Tomas') #видаєя елемент який записаний в дужках
print(name)

print('index', name.index('Nick')) #показує індекс конкретного елемента що вказаний в дужках

name.pop(1) #видаляє елемент по вказаному індексу
print(name)

print(array2)
print(array2.count(1)) # показує кількість повторів вказаного елемента

array2.sort(reverse=True) #сортування списка від меншого до більшого. Вдужках можна задати ф-ю сортування
print(array2)

array2.reverse() #елементи списка в зворотньому порядку
print(array2)

a = max(array2)
b = min(array2)
print(a, b)

print(array)
array[3] = 56
c = sorted(array, reverse=True)
print(c)