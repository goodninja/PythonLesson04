# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов. 
# 2*x² + 4*x + 5 3*x² +10*x + 6 Вывод: 5*x² + 14*x + 11


import sympy
from random import randint

def polynomial_creation(degree):
    x = sympy.Symbol('x')
    result = ((randint(0,10))*x + (randint(0,10)))**degree
    result = str(sympy.expand(result))
    return result

def write_file(file,str):
    path = file
    data = open(path,'w')
    data.write(str)
    data.close()

def sum_of_2_polynomial(file1, file2):
    with open(file1) as first:
        first_file = first.read()
    with open(file2) as second:
        second_file = second.read()
    x = sympy.Symbol('x')
    summary = first_file + " + " + second_file
    summary = str(sympy.collect(summary,x))
    return summary

def run_functions():
    
    a = randint(1,5)
    b = randint(1,5)
    
    a_path = 'C:/Users/Bjorn Hatred/Desktop/THE MOST IMPORTANT FOLDER/GeekBrains/Python/Lesson04/task05/file1.txt'
    b_path = 'C:/Users/Bjorn Hatred/Desktop/THE MOST IMPORTANT FOLDER/GeekBrains/Python/Lesson04/task05/file2.txt'
    res_path = 'C:/Users/Bjorn Hatred/Desktop/THE MOST IMPORTANT FOLDER/GeekBrains/Python/Lesson04/task05/output.txt'
    
    a_poly = polynomial_creation(a)
    b_poly = polynomial_creation(b)
  
    write_file(a_path,a_poly)
    write_file(b_path,b_poly)

    res = sum_of_2_polynomial(a_path,b_path)

    write_file(res_path, res)
    print('CONGRATULATIONS! MISSION ACCOMPLISHED \n file has been written')

run_functions()