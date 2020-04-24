"""56. Якщо в одновимірному масиві є три поспіль однакових елемента, то
змінній r привласнити значення істина."""
from random import  randint
A = list()
p = -500
t = 0
flag = False
for n in range(1000):
    A.append(randint(-50,50))
for n in range(len(A)):
    if A[n] == p:
        t+=1
    else:
        p = A[n]
        t = 1
    if t == 3:
        flag = True
print(flag)
