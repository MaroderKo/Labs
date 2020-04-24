"""44. Підрахуйте кількість елементів одновимірного масиву, які збігаються зі
своїм номером і при цьому кратні 3."""
from random import randint
A = list()
sum = 0
for n in range(10):
    A.append(randint(0, 10))
    if A[n] == n and A[n]%3==0:
        sum+=1
print(sum)