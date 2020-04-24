"""40. Обчислити суму парних елементів одновимірного масиву до першого
зустрінутого нульового елемента."""
from random import randint
A = list()
flag = False
sum = 0
for n in range(100):
    A.append(randint(-20, 20))
    if A[n] == 0:
        flag == True
    if not flag and A[n]%2 ==0:
        sum +=1
print(sum)