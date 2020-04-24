"""31. Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які потрапляють в інтервал від -2 до 10."""
from random import randint
A = list()
count = 0
sum = 0
for n in range(1000):
    A.append(randint(5, 100))
    if -2<=A[n]<=10:
        sum += A[n]
        count+=1
print(sum/count)