"""60. Дан одновимірний масив з 10 цілих чисел. Підрахуйте найбільше число
однакових чисел, що йдуть підряд в ньому."""
from random import  randint
A = list()
p = -500
t = 0
max = 0
for n in range(1000):
    A.append(randint(-50,50))
for n in range(len(A)):
    if A[n] == p:
        t+=1
    else:
        p = A[n]
        t = 1
    if t > max:
        max = t
print(max)
