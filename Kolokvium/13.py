"""13. Створіть масив з 15 цілочисельних елементів і визначте серед них
мінімальне значення."""
from random import randint
A = list()
for n in range(15):
    A.append(randint(0,100))
# Создание масива
min = 0
for n in range(len(A)):
    if A[n]<max:
        min = A[n]
# Поиск минимального значения
print(min)