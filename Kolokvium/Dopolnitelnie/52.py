"""52. Знайти найбільший елемент з елементів одновимірного масиву, що мають
парний номер. Визначити, чи є він єдиним."""
from random import randint
A = list()
max = -50
edin = True
t = False
for n in range(10):
    A.append(randint(-30, 30))
for n in range(0,10,2):
    if A[n] > max:
        max = A[n]
        edin = True
    elif A[n] == max:
        edin = False
print(max,"  ",edin)