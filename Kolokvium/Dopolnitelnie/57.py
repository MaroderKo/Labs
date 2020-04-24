"""57. Відомість на зарплату представлена як дві таблиці. Одна містить
прізвища працівників цеху, а друга - їх зарплату за поточний місяць. Знайдіть прізвище
працівника, зарплата якого найменш відхиляється від середньої зарплати всіх
працівників за поточний місяць. Знайдіть прізвища двох працівників з найбільшою
заробітною платою. Видаліть з відомості на зарплату відомості про працівника,
зарплата якого мінімальна."""
import random
A = list()
B = list()
sum = 0
N = int(input())
for n in range(N):
    A.append(str(random.randint(-5,15)))
    B.append(random.randint(100,15000))
    sum+=B[n]
avg = sum//N
min = 1000000;
mini = -1;
for n in range(N):
    if min >abs(avg-B[n]):
        min = abs(avg - B[n])
        mini = n
print(A[mini])
for i in range(2):
    maxy = max(B)
    maxw = A[B.index(maxy)]
    print(f"Bigest paymant {maxy}uah. {maxw}")
    A.remove(maxw)
    B.remove(maxy)