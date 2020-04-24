"""49. Задано дві таблиці. Одна містить найменування послуг, а інша - розцінки
за ці послуги. Видаліть з обох таблиць все, що передує послузі, ціна якої G гривень."""
import random
A = list()
B = list()
N = int(input())
for n in range(N):
    A.append(str(random.randint(-5,15)))
    B.append(random.randint(100,15000))
if N in B:
    global t
    t = B.index(N)
    for n in range(t):
        A.remove(A[0])
        B.remove(A[0])