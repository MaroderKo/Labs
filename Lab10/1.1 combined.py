"""
1. Сформувати функцію, що буде обчислювати факторіал заданого користувачем
натурального числа n.
Виконав: Перепелиця А.С.
"""
from datetime import datetime


def factorial(a): #Рекурсия
    global sum #глобальный вызов переменной
    sum *= a #домножение числа
    if a != 1: #число всегда делится на один а ноль уже уничтожит результат
        factorial(a - 1) #Заход на рекурсию
    else:
        return 1


var = int(input("Рекрсивная версия(1) или иерационная(2): "))
if var == 1:
    a: int = int(input()) # ввод начальных значений значений
    sum: int = 1
    start_time = datetime.now()
    factorial(a)#Заходна функцию с элементом рекурсии
    print(sum)  # вывод суммы
    print(datetime.now() - start_time)  # Вывод времени
else:
    a: int = int(input())
    sum: int = 1
    start_time = datetime.now()
    while a!=1: #Нерекурсивная функция
        sum*=a #Домножение
        a-=1 #Итерационный ход
    print(sum) #вывод суммы
    print(datetime.now() - start_time) #Вывод времени
