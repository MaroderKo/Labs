"""19. Знайти суму всіх елементів масиву цілих чисел що задовольняють умові:
остача від ділення на 2 дорівнює 3. Розмірність масиву - 20. Заповнення масиву
здійснити випадковими числами від 200 до 300."""
from random import randint
A = list()
sum = 0
for n in range(20):
    A.append(randint(200, 300))
    # Создание масива
    if A[n] % 2 == 3:
        sum += A[n]
    # Подсчёт данных по фильтру
print(sum)
