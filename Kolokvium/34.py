"""34. Дано два лінійних масиву однакової розмірності. Скласти третій масив з
добутку елементів перших двох масивів, що стоять на місцях з однаковим індексом."""
from random import randint
A = list()
B = list()
C = list()
sum = 0
for n in range(20):
    A.append(randint(-3, 10))
    B.append(randint(-3, 10))
    C.append(A[n]*B[n])
print(C)