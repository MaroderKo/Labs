"""43. Задано два натуральних числа a і b. Змінній w привласнити значення
істина, якщо в одновимірному цілочисельному масиві є хоча б один елемент, кратний а
і не кратний b."""
from random import randint
A = list()
a = int(input())
b = int(input())
w = False
for n in range(10):
    A.append(randint(-50, 50))
    if A[n] % a == 0 and A[n]%b!=0:
        w = True
        break
print(w)