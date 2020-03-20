import numpy as np
#
#1. Напишіть програми, що виконують такі операції з масивами (використовувати
#вбудовані методи по роботі з масивами заборонено):
# виведіть на екран елементи лінійного масиву (заданий користувачем) у
#зворотному порядку;
# виведіть на екран транспоновану матрицю 3*3 (початкова матриця задана
#користувачем).
# виконайте добуток двох квадратних матриць 3*3, врахуйте розмірність.
#Результати множення елементів занесіть до нової матриці та виведіть її на екран;
# у матриці 4*4, що задана користувачем замініть всі від’ємні елементи на 0.
#1.1
print("Виберiть номер для перевiрки:")
p = input()
if p == "1.1":
    a = []
    el = input()
    a = list(map(int,el.split()))
    s1 = len(a)-1
    while(s1!=-1):
        print(a[s1])
        s1-=1
#1.2
elif p == "1.2":
    a11 = np.zeros([3,3],dtype=int)
    for n in range(3):
        for g in range(3):
            a11[n][g] = input("Введiть значення в клiтинку ["+str(n+1)+"] ["+str(g+1)+"]:")
    a1 = np.zeros([3,3],dtype=int)
    for i in range(3):
        for j in range(3):
            a1[i][j] = a11[j][i]
    print(a1)
#1.3
elif p=="1.3":
    a = np.zeros([3,3],dtype=int)
    a1 = np.zeros([3,3],dtype=int)
    for n in range(3):
        for g in range(3):
            a[n][g] = input("Введiть значення в клiтинку ["+str(n+1)+"] ["+str(g+1)+"]:")
    for n in range(3):
        for g in range(3):
            a1[n][g] = input("Введiть значення в клiтинку ["+str(n+1)+"] ["+str(g+1)+"]:")
    b = np.zeros([3,3],dtype=int)
    for i in range(len(a)):
       for j in range(len(a1[0])):
           for k in range(len(a1)):
               b[i][j] += a[i][k] * a1[k][j]
    print(b)
elif p == "1.4":
#1.4
    a = np.zeros([4,4],dtype=int)
    for n in range(4):
        for g in range(4):
            a[n][g] = input("Введiть значення в клiтинку ["+str(n+1)+"] ["+str(g+1)+"]:")
    for n in range(4):
        for g in range(4):
            a[n][g] = 0 if a[n][g] <=0 else a[n][g]
    print(a)