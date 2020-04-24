"""42. Підрахувати кількість елементів одновимірного масиву, для яких
виконується нерівність i*i<ai<i!"""
from random import randint
A = list()
sum = 0
for n in range(10):
    A.append(randint(-50, 50))
    if n*n <A[n]<n:
        sum+=1
print(sum)