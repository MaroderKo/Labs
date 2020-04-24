"""30. Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які розташовані за першим по порядку мінімальним елементом."""
from random import randint
A = list()
min = 101
sum = 0
for n in range(1000):
    A.append(randint(5, 100))
    if A[n] < min:
        min = A[n]
for n in range(len(A)):
    if A[n] == min:
        global tr
        tr = n
        break
for n in range(tr+1):
    sum+=A[n]
print(sum/(tr+1))