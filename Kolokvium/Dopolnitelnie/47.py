"""47. У лінійному масиві знайти максимальний елемент. Вставте порядковий
номер елемента за ним, пересунувши всі залишилися на одну позицію вправо."""
from random import randint
A = list()
B = list()
max = -50
for n in range(10):
    A.append(randint(-30, 30))
    if A[n] > max:
        max = A[n]
for n in range(len(A)):
    B.append(A[n])
    if A[n] == max:
        B.append(n)