from modul_def import calculation_salary
from modul_def import list_more_then
from modul_def import unig_list
from modul_def import unig_values
from modul_def import sum_list
from itertools import count, cycle
from modul_def import fibo_gener



print("Задание № 1")
clok = int(input("введите кол-во часов: "))
tarif = int(input("введите тариф: "))
bonus = int(input("введите % преми (целое число): "))
calculation_salary(clok, tarif, bonus)

print("Задание № 2")
rng = int(input("задайте длинну списка: "))
dp = int(input("задайте диапазан случайных чисел от 0 до: "))

list_more_then(rng, dp)


print("Задание № 3")
print("Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.")
print(unig_list())

print("Задание № 4")
print("Представлен список чисел. Определить элементы списка, не имеющие повторений.")
print(unig_values())

print("Задание № 5")
print("Реализовать формирование списка c четныvb числаvb от 100 до 1000 (включая границы).") 
print("получить результат вычисления произведения всех элементов списка.")
print(sum_list())

print("Задание № 6\nРеализовать два небольших скрипта:")
print("а - бесконечный итератор, генерирующий целые числа, начиная с указанного")
print("б - бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.")

print("Для работы скрипта 'а' нажмите 'enter', для выхода 'q'")
for i in count(int(input("введите начальное число: "))):
    print(i,end='')
    quit = input()
    if quit == 'q':
        break
        
print("Для работы скрипта 'б' нажмите 'enter', для выхода 'q'")
u_list = input("введите список разделяя элементы пробелом").split()
iter = cycle(u_list)
quit = None
while quit != 'q':
    print(next(iter), end='')
    quit = input()


print("Задание № 7\nРеализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.")

x = int(input("введите число до которого считаем факториал, но не боьше 15: "))

for i in fibo_gener(x):
    print(i)