"""2. Введіть з клавіатури п'ять цілочисельних елементів масиву X. Виведіть на
екран значення коріння і квадратів кожного з елементів масиву."""
import numpy as np
import math
a = np.zeros(5,dtype=int)
#Создание масива
for n in range(5):
    a[n] = int(input())
#Ввод масива
for n in a:
    print(math.sqrt(n)+" "+math.pow(n,2))
#Вывод результатов