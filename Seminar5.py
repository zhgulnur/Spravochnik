# Урок 7. Лекция. Функции, рекурсия, алгоритмы

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# # Выводим первые 10 чисел Фибоначчи
# list1 = []
# for i in range(10):
#     list1.append(fibonacci(i))
# print(list1)


# Урок 8. Семинар. Рекурсия и алгоритмы
# Ex 1
'''Требуется найти N-е число Фибоначчи
Input: 7
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
Output: 8'''

# def fibonacci(n):
#     if n <=1:
#         return n
#     else: 
#         return fibonacci(n-1) + fibonacci(n-2)

# n = int(input('Введите n: '))
# print(fibonacci(n-1)) 

# # индексация чисел Фибоначчи начинается с 0, а не с 1. 
# # Таким образом, если вы хотите получить седьмое число Фибоначчи, нужно вызвать 
# # fibonacci(6), а не fibonacci(7)

# Ex 2
'''Хакер Василий получил доступ к классному журналу и хочет заменить все свои 
минимальные оценки на максимальные. Напишите программу, которая заменяет оценки 
Василия, но наоборот: все максимальные – на минимальные.

Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1'''

# import random
# n = int(input("How many grades does Vasiliy have? "))
# arr = [random.randint(1,5) for i in range(n)]
# print(f"Initial grades: {arr}")

# def replace_mark(list1):
#     i = 0
#     min_val = 10
#     max_val = -1
#     for i in range(len(list1)):
#         if list1[i] < min_val:
#             min_val = list1[i]
#         elif list1[i] > max_val:
#             max_val = list1[i]
#         i += 1
    
#     for i in range(len(list1)):
#         if list1[i] == max_val:
#             list1[i] = min_val
    
#     return list1

# print(f"Changed grades: {replace_mark(arr)}")


# Ex 3
'''Напишите функцию, которая принимает на вход одно число и проверяет, является ли оно 
простым. Простые числа делятся только на 1 и на себя'''

# # my solution (very straighworward):
# def simple_num(n):
#     if n == 2 or n ==3 or n == 5:
#         return 'yes'
#     elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
#         return 'no'
#     return 'yes'

# # Chat GPT's solution:
# def simple_num(number):
#     if number < 2:
#         return 'no'
#     for i in range(2, number): # можно заменить на range(2, int(number**0.5) + 1) 
#         # потому что если число делится на какое-то число i больше его квадратного 
#         # корня, то оно также будет делиться на число, меньшее чем квадратный корень, 
#         # и проверка уже была бы проведена на этапе проверки меньших чисел.
#         if number % i == 0:
#             return 'no'
#     return 'yes'

# num = int(input("Enter your number: "))
# print(simple_num(num))


# Ex 4
'''Дано натуральное число N и последовательность из N элементов. 
Требуется вывести эту последовательность в обратном порядке.

Запрещается объявлять массивы и использовать циклы (даже для ввода и вывода)

Input: 2 -> 3 4
Output: 4 3'''

# import random
# def reverse_sequence(n):
#     if n == 0:
#         return ""
    
#     k = int(input())
#     return reverse_sequence(n-1) + f"{k} "

# n = int(input("How many numbers do you have: "))
# print(reverse_sequence(n))



##### HOMEWORK

# Ex 1
'''Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую 
степень b с помощью рекурсии.

Функция не должна ничего выводить, только возвращать значение.

Пример:
a = 3; b = 5 -> 243 (3⁵)
a = 2; b = 3 -> 8 '''

# def exponent(a,b):
#     if b == 0: 
#         return 1
#     return a * exponent(a, b-1)

# a = int(input('Enter the first number: '))
# b = int(input('Enter the second number: '))
# print(f'a^b = {a}^{b} = {exponent(a,b)}')



# Ex 2
'''Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

Функция не должна ничего выводить, только возвращать значение.
sum(2, 2)
# 4
'''

# a = int(input('Enter the first number: '))
# b = int(input('Enter the second number: '))

# def sum(a,b):
#     if b == 0:
#         return a
#     return 1 + sum(a, b-1)
# # мы сначала суммируем b с помощью "1+", а потом прибавляем целый а, когда заканчивается b

# print(sum(a,b))
