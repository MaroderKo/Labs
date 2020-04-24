"""29. Знайти кількість парних елементів одновимірного масиву до першого
зустрінутого числа рівного наперед заданому числу а."""
from random import randint
A = list()
flag = False
a = int(input("Задане число:"))
sum = 0
for n in range(100):
    A.append(randint(50, 100))
    if A[n] == a:
        flag == True
    if not flag and A[n]%2 ==0:
        sum +=1
print(sum)