"""17. Знайти суму елементів масиву дійсних чисел, що мають непарні номери.
Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами від 100
до 200."""
from random import randint
A = list()
sum = 0
for n in range(20):
    A.append(randint(100,200))
    # Создание масива
    if A[n]%2!=0:
        sum +=A[n]
    # Подсчёт данных по фильтру
print(sum)