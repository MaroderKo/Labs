"""33. Заданий масив А (1:20). Знайти добуток всіх його ненульових елементів."""
from random import randint
A = list()
sum = 0
for n in range(20):
    A.append(randint(-3, 10))
    if A[n] !=0:
        sum +=1
print(sum)