# Вычислить число Пи c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

def pi_calculation(d_factor):
    if d_factor<=-1 and d_factor>=-10:
        x = str(math.pi)
        print(f'Число Пи с заданной точностью d = {x[:2+abs(d_factor)]}')
    else:
        print("Задайте точность d от -1 до -10")

def input_degree():
    degree = int(input('Введите от -1 до -10 (точность для d, количество цифр после точки): '))
    pi_calculation(degree)

input_degree()