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


a: int = int(input()) # ввод начальных значений значений
sum: int = 1
start_time = datetime.now()#Начало записи аремени
factorial(a)  # Заходна функцию с элементом рекурсии
print(sum) #вывод суммы
print(datetime.now() - start_time) #Вывод времени
