# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def mult_list_N(n):
    if n > 0:
        result = ""
        for i in range(1,n+1):
            if n % i == 0:
                result += str(i) + " "
        print(f'Список простых множителей числа {n} -> [{result}]')
    else:
        print("Задайте натуральное число")

def input_N():
    num = int(input('Введите натуральное число N: '))
    mult_list_N(num)

input_N()