"""1. Введіть з клавіатури в масив п'ять цілочисельних значень. Виведіть їх в
один рядок через кому. Отримайте для масиву середнє арифметичне."""
import numpy as np
a = np.zeros(5,dtype=int)
sum = 0
#Звполнение масива
for n in range(5):
    a[n] = int(input())
    sum+=a[n]
#Вывод результатов
b = str(a)[1:-1].replace(" ", ", ")
print(b)
print(sum/5)