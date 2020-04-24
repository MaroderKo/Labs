"""41. Змінній t привласнити значення істина, якщо максимальний елемент
одновимірного масиву єдиний і не перевищує наперед заданого числа а."""
from random import randint
A = list()
flag = False
a = int(input("Задане число:"))
max = -50
edin = True
t = False
for n in range(10):
    A.append(randint(-30, 30))
    if A[n] > max:
        max = A[n]
        edin = True
    elif A[n] == max:
        edin = False
if max <= a and edin:
    t = True
print(t)