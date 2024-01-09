# Урок 9. Семинар. Повторение списков
import random
# Ex 1
'''Даны два массива чисел. Требуется вывести элементы первого массива (в том порядке, 
в каком они идут в первом массиве), которых нет во втором массиве.

Входные данные

Записано сначала число N - количество элементов в первом массиве, затем N чисел - элементы массива. 
Затем записано число M – количество элементов во втором массиве. Затем записаны элементы второго 
массива. Количество элементов каждого массива не превышает 100. Сами элементы -числа из диапазона 
int.

Выходные данные

Выведите те элементы первого массива, которых нет во втором в том порядке, в каком они идут 
в первом массиве.

Пример

Вход 
7
3 1 3 4 2 4 12
6
4 15 43 1 15 1

Выход
3 3 2 12'''

# n = int(input("How many numbers in the first array? "))
# list1 = [random.randint(1,10) for i in range(n)]
# print(list1)
# m = int(input("How many numbers in the second array? "))
# list2 = [random.randint(1,10) for i in range(m)]
# print(list2)

# count = 0
# for i in range(n):
#     for j in range(m):
#         if list1[i] == list2[j]:
#             count += 1
#     if count == 0:
#         print(list1[i])
#     count == 0 


# Ex 2
'''Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит 
количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного.

Входные данные
Сначала задано число N — количество элементов в массиве (1<N<100). Далее через пробел записаны 
N чисел — элементы массива. Массив состоит из целых чисел.

Выходные данные
Необходимо вывести количество элементов массива, у которых два соседа и которые при этом строго 
больше обоих своих соседей.

Примеры
входные данные
5
1 2 3 4 5

выходные данные
0
входные данные
5
1 5 1 5 1

выходные данные
2'''
            
# n = int(input("How many numbers in the array? "))
# list1 = [random.randint(1,10) for i in range(n)]
# print(list1)  

# count=0
# for i in range(1, n-1):
#     if list1[i] > list1[i-1] and list1[i] > list1[i+1]:
#         count += 1
# print(count)


# Ex 3
'''Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
Считается, что любые два элемента, равные друг другу образуют одну пару, которую 
необходимо посчитать.

Input:
1 2 3 2 3 

Output: 2
'''
# n = int(input("How many numbers in the array? "))
# list1 = [random.randint(1,10) for i in range(n)]
# print(list1)  
# # list1 = [3, 7, 8, 8, 8, 3, 7, 8]
# # n = 8

# count = 0
# for i in range(n):
#     for j in range(i+1, n):
#         if i!= j and list1[i] == list1[j]:
#             count += 1

# print(count)

# # Чтобы не было такой ошибки как в зелененьких:
# # count = 0
# # used_indices = set()  # Множество для отслеживания уже использованных индексов

# # for i in range(n):
# #     for j in range(i + 1, n):
# #         if list1[i] == list1[j] and i not in used_indices and j not in used_indices:
# #             count += 1
# #             used_indices.add(i)
# #             used_indices.add(j)


# Ex 4
'''Два натуральных числа называются дружественными, если каждое из них равно сумме всех 
делителей другого (само другое число в качестве делителя не рассматривается). Например, 
220 (1+2+4+5+10+11+20+22+44+55+110=284) и 284 (1+2+4+71+142=220) – дружественные числа. 
Пары необходим о выводить по одной в строке, разделяя пробелами. Найти все пары натуральных 
дружественных чисел, меньших k.'''

# k = int(input("Enter your number: "))
# list1 = list()

# for i in range(k):
#     sum = 0
#     for j in range(1, i//2 + 1):
#         if i%j==0:
#             sum += j
#     list1.append(tuple([i, sum]))

# for i in range(k):
#     for j in range(i, k):
#         if i!=j and list1[i][0] == list1[j][1] and list1[i][1] == list1[j][0]:
#             print(*list1[i])



### HOMEWORK
# Ex 1
'''Определить индексы элементов массива (списка), значения которых принадлежат заданному 
диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).
На вход подается список с элементами list_1 и границы диапазона в виде чисел min_number, 
max_number.

На входе:
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

На выходе:
1
2
3
6
7
9
10
11
13
14
16
19'''

# n = int(input("How many numbers do you want to have in your list? "))
# list1 = [random.randint(-20,20) for i in range(n)]

# min_number = int(input("What is your min number? "))
# max_number = int(input("What is your max number? "))

# print(list1)

# for i in range(n):
#     if min_number <= list1[i] <= max_number:
#         print(i)


# Ex 2
'''Заполните массив элементами арифметической прогрессии. Её первый элемент a1 , 
разность d и количество элементов n будет задано автоматически. Формула для получения 
n-го члена прогрессии: an = a1 + (n-1) * d.

На входе:
a1 = 2
d = 3
n = 4

На выходе:
2
5
8
11'''

# a1 = int(input("Enter the first number of arithmethic progression: "))
# d = int(input("Enter the difference: "))
# n = int(input('Enter the size of arithmetic progression: '))

# list1 = list()

# for i in range(n):
#     list1.append(a1 + i * d)

# for elem in list1:
#     print(elem)