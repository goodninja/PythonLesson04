# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import sympy                        # sympy module must be installed
from random import randint

def polynomial_creation(degree):
    if degree > 0:
        x = sympy.Symbol('x')
        result = ((randint(0,10))*x + (randint(0,10)))**degree
        result = str(sympy.expand(result)) + " = 0"
        print(result)
        return result
    else:
        print("Должна быть задана натуральная степень")

def write_file(str):
    path = 'C:/Users/Bjorn Hatred/Desktop/THE MOST IMPORTANT FOLDER/GeekBrains/Python/Lesson04/task04/output.txt'
    data = open(path,'w')
    data.write(str)
    data.close()

def input_k():
    k =int(input('Задайте натуральную степень k: '))
    answer = polynomial_creation(k)
    write_file(answer)

input_k()