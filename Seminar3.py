# Урок 5. Семинар. Списки и словари

# Ex 1
# '''Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input [1,1,2,0,-1,3,4,4]
# Output: 6'''

# mylist = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(mylist)))


# Ex 2
'''Дана последовательность из N целых чисел и число K. 
Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
на K элементов вправо. K - положительное число

Input: [1, 2, 3, 4, 5] k = 3
Output: [3, 4, 5, 1, 2]
'''

# input_string = input('Введите элементы списка через пробел: ')
# k = int(input('Введите k: '))
# mylist = [int(item) for item in input_string.split()]
# # mylist = input_string.split()  # если это строки
# print(mylist)

# # for case if k is larger than the length of the list:
# k = k % len(mylist)
# n = k
# list_res = []

# for i in range(k):
#     list_res.append(mylist[len(mylist) - n])
#     n -= 1
# print(list_res)

# for i in range(len(mylist) - k):
#     list_res.append(mylist[i])
# print(list_res)

# # Solution from Chat GPT:
# for i in range(len(mylist) - k, len(mylist)):
#     list_res.append(mylist[i])

# for i in range(0, len(mylist) - k):
#     list_res.append(mylist[i])

# print(list_res)


# Ex 3
'''Напишите программу на Python для печати всех уникальных значений в словаре.
Исходный список: [{'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, {'VI': 'S005'}, 
{'VII': ' S005 '}, {' V ':' S009 '},{'VIII': 'S007'}]                                                                                            
Уникальные значения: {'S009', 'S002', 'S007', 'S005', 'S001'}'''

# list1 = [{'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, {'VI': 'S005'}, 
#          {'VII': ' S005 '}, {' V ':' S009 '},{'VIII': 'S007'}]
# set_1 = set()

# for i in list1:
#     for j in i:
#         set_1.add(i[j].strip())

# print(set_1)
    

# Ex 4
'''Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает
количество элементов массива, больших предыдущего (элемента с предыдущим
номером).

Input [0, -1, 5, 2, 3]
Output 2 (-1<5, 2<3)'''

# input_string = input('Введите элементы списка через пробел: ')
# mylist = [int(item) for item in input_string.split()]

# count = 0

# for i in range(len(mylist)-1):
#     if mylist[i] < mylist[i+1]:
#         count += 1

# print(count)


##########  ДОМАШКА 

# Ex 1
''' Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
Найдите количество и выведите его.

list_1 = [1, 2, 3, 4, 5]
k = 3
# 1   '''

# import random
# n = int(input('Введите количество элементов в массиве: '))
# mylist = [random.randint(1, 10) for i in range(n)]
# k = int(input('Введите интересующее число: '))
# print(mylist)
# count = 0

# for i in mylist:
#     if i == k:
#         count +=1

# print(count)


# Ex 2
'''Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k 
и вывести его.
Считать, что такой элемент может быть только один. 
Если значение k совпадает с этим элементом - выведите его.

list_1 = [1, 2, 3, 4, 5]
k = 6
# 5 '''

# import random
# n = int(input('Введите количество элементов в массиве: '))
# mylist = [random.randint(1, 10) for i in range(n)]
# mylist = set(mylist)
# mylist = list(mylist)
# k = int(input('Введите интересующее число: '))
# number = mylist[0]

# for i in mylist:
#     if abs(i-k) < abs(number-k):
#         number = i

# print(mylist)
# print(number)


# Ex 3
'''В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.

А русские буквы оцениваются так:
А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова k и 
выводит его. Будем считать, что на вход подается только одно слово, которое содержит 
либо только английские, либо только русские буквы.'''


# k = str(input("Enter your word in Eglish or Russian: "))
# k = k.upper() 
# print(k)
# count = 0 

# eng_dict = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1, 
#             'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3,  'F': 4, 'H': 4, 'V': 4, 'W': 4, 
#             'Y': 4, 'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10}

# rus_dict = {'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1, 'Д': 2, 
#             'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2, 'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3, 
#             'Й': 4, 'Ы': 4, 'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5, 'Ш': 8, 'Э': 8, 'Ю': 8, 
#             'Ф': 10, 'Щ': 10, 'Ъ': 10}

# for i in k:
#     for (key, value) in eng_dict.items():
#         if i == key:
#             count += value
#     for (key, value) in rus_dict.items():
#         if i == key:
#             count += value


# print(count)









