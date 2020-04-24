"""28. Знайти кількість парних елементів одновимірного масиву."""
#Який масив я не поняв, тому роблю рандомний на 50 значень
from random import randint
A = list()
sum = 0
for n in range(50):
    A.append(randint(50, 1000))
    if A[n] %2==0:
        sum+=1
print(sum)
