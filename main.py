# 1.Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# N=input("Введите число:")
# sum=0
# while N!=0:
#     i=N%10
#     sum+=i
#     N=N//10
# print (sum)

# number= input("Введите число:")
# summa=0
# for i in number:
#     if i.isdigit():
#         summa+=int(i)
# print(summa)

# from decimal import Decimal
# number = Decimal(input('Введите число: '))
# def sum_digits(number: int):
#     summa=0
#     while number >0:
#         summa += number%10
#         number//=10
#     return summa
# while (number != int (number)):
#     number*=10
# print(number)
# summa=sum_digits(number)
# print (f'Сумма чисел равна {int(summa)}')


# 2. Задайте список из n чисел последовательности (1 + 1/n)^n.
# Вывести в консоль сам список и сумму его элементов.

# n=int(input("Введите число:"))
# big_list=range(1,n+1)
# my_list=[]
# sum=0
# for i in big_list:
#     j=(1+1/i)*i
#     print(j)
#     my_list.append(i)
#     sum += i
# print(my_list)
# print(sum)


# 3. Реализуйте алгоритм перемешивания списка.
# Встроенный алгоритм SHUFFLE не использовать!
# Реализовать свой метод

import random
my_list= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list)
for i in range(len(my_list)):
    n= random.randint(0, len(my_list)-1)
    my_list.append(my_list.pop(n))
print(f'Перемешанный список {my_list}')


