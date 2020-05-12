"""
3. Сформувати функцію для обчислення індексу максимального елемента масиву
n*n, де 1<=n<=5.
Виконав: Перепелиця А.С.
"""
from datetime import datetime
import random
import numpy as np

b = int(input()) # ввод начальных значений значений
a = list()
start_time = datetime.now()#Начало записи аремени
###########
for n in range(b):
    a.append(np.zeros(b, dtype=int))
for n in range(b):
    for p in range(b):
        a[n][p] = random.randint(-100, 100)
########### Создание и заполнение массива
max = -200 #начальное значение максимума
for n in range(b): #цыкл
    for p in range(b): #цыкл
        if a[n][p] > max: #Сравние с максимумом
            max = a[n][p]
            coords = [n + 1, p + 1]
print(max) # вывод результата
print(coords) # вывод результата
print(datetime.now() - start_time) #Вывод времени
