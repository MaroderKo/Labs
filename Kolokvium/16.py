"""16. Знайти добуток елементів масиву цілих чисел, які кратні 7. Розмірність
масиву - 15. Заповнення масиву здійснити випадковими числами від 10 до 50."""
from random import randint
A = list()
dob = 1
for n in range(15):
    A.append(randint(10,50))
    # Создание масива
    if A[n]%7==0:
        dob *=A[n]
    # Подсчёт данных по фильтру
print(dob if dob!=1 else str(0))