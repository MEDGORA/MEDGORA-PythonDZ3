"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

n = 5
1 2 3 4 5
x = 6
-> 5
"""
n = int(input('Введите количество элементов в массиве N: '))
i = 0
list1 = [0] * n

for i in range(n) :
  print('Введите',i + 1,'-й элемент массива')
  list1[i] = int(input())
  i += 1

x = int(input('Введите число X: '))
list2 = [0] * n

for i in range(n) :
    list2[i] = abs(x - list1[i])
    i += 1

minDifferenceIndex = 0

for i in range(n-1) :
    if list2[i] > list2[i+1] :
        Difference = i+1
    i += 1
print('Число',list1[Difference],'самое близкое к числу Х =',x)