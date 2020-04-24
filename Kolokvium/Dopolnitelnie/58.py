"""58. Дан одновимірний масив цілих чисел. Знайдіть, скільки разів в ньому
повторюється найчастіше число."""
from random import randint
A = list()
max = 0
for n in range(15):
    A.append(randint(-100,100))
d = dict()
for n in range(15):
    if A[n] in d.keys():
        temp = d.get(A[n])
        d[A[n]] = temp+1
        if max < d.get(A[n]):
            max = d.get(A[n])
    else:
        d[A[n]] = 1
        if max < d.get(A[n]):
            max = d.get(A[n])
print(max)
print(d.values())
