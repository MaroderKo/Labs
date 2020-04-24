"""32. Змінній t привласнити значення істина, якщо в одновимірному масиві є
хоча б одне від’ємне і парне число."""
from random import randint
t = False
A = list()
for n in range(100):
    A.append(randint(-3, 100))
    if A[n] < 0 and A[n]%2==0:
        t = True
print(t)