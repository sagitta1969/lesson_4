from random import randint
from functools import reduce
from math import factorial
from itertools import count, cycle


def calculation_salary(clok, tarif, bonus):
    '''Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. 
    В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.'''
    
    salary = (clok * tarif)+ (clok * tarif * bonus) / 100
    #return(salary)
    print(salary)

def list_more_then(x, y):
    ''' Представлен список чисел. Необходимо вывести элементы исходного списка, 
        значения которых больше предыдущего элемента.'''
    
    a = [randint(0, y) for i in range(x)]
    b = []
    for i in range(len(a) - 1):
        if a[i] < a[i + 1]:
            b.append(a[i + 1])
    print(a)
    print(b)

def unig_list():
    ''' Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. 
        Необходимо решить задание в одну строку.'''
    
    b = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
    return(b)

def unig_values():
    ''' Представлен список чисел. Определить элементы списка, не имеющие повторений. 
        Сформировать итоговый массив чисел, соответствующих требованию. 
        Элементы вывести в порядке их следования в исходном списке.'''
    my_list = [randint(-10, 10) for i in range(20)]
    unig_list = [el for el in my_list if my_list.count(el) == 1]
    print(f"исходный список\n{my_list}\nуникальные значения\n{unig_list}")

def sum_list():
    ''' формирует список четных значений от 100 до 1000, 
        выводит произведение всех значений списка'''
    a = list(range(100, 1001, 2))
    b = reduce(lambda x,y: x * y, a)
    return a, b

def fibo_gener(n):
    ''' Функция отвечает за получение факториала числа, 
        а в цикле необходимо выводить только первые 15 чисел.'''
    m = 1
    for i in range (1, n):
        if i > 15:
            print("вы ввели число больше 15")
            break
        m *= i
        yield m
