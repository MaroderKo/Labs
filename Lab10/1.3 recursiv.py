"""
3. Сформувати функцію для обчислення індексу максимального елемента масиву
n*n, де 1<=n<=5.
Виконав: Перепелиця А.С.
"""
import random
import numpy as np
from datetime import datetime


def do(a):
    # # # # # # # # # #
    global coords
    global max
    global b
    global c
    # # # # # # # # # # вызов глобальных переменных
    if c != (b):
        for n in range(b):
            if a[c][n] > max: #сравнение
                max = a[c][n]
                coords = [c + 1, n + 1]
        c += 1 #рекурсивная итерация
        do(a) #рекурсивный вызов


b = int(input()) # ввод начальных значений значений
a = list()
coords = list()
start_time = datetime.now()#Начало записи аремени
###########
for n in range(b):
    a.append(np.zeros(b, dtype=int))
for n in range(b):
    for p in range(b):
        a[n][p] = random.randint(-100, 100)
########### Создание и заполнение массива
max = -200 #начальное значение максимума
c = 0
do(a)
print(max) # вывод результата
print(coords) # вывод результата
print(datetime.now() - start_time) #Вывод времени
