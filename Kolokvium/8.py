"""8. Створіть цілочисельний масив А [1..15] за допомогою генератора
випадкових чисел з елементами від -15 до 30 і виведіть його на екран. Визначте
найбільший елемент масиву і його індекс."""
from random import randint
A = list()
for n in range(15):
    A.append(randint(-15,30))
#Создание масива
print(A)
max = -16
ind = -1
#Задание начальных данных которые не повияют на обсчёт
for n in range(15):
    if A[n] >max:
        ind = n
        max = A[n]
