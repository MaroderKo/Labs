"""25. Знайти добуток елементів лінійного масиву цілих чисел, які кратні 5.
Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами від 10 до
100."""
from random import randint
A = list()
sum = 1
for n in range(10):
    A.append(randint(10, 100))
    # Создание масива
    if A[n] %5 == 0:
        sum *= A[n]
    # Подсчёт данных по фильтру
print(sum)