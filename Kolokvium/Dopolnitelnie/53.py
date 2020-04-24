"""53. В масиві X (1: n) кожен елемент рівний 0, 1 або 5. Переставити елементи
масиву так, щоб спочатку розташовувалися всі нулі, потім все одиниці, а потім всі
п'ятірки. Додаткового масиву не заводити."""
from random import  randint
import numpy as np
def bubbles_sort(array):
    global kol_vo_sravneniy
    global kol_vo_zamen
    kol_vo_sravneniy = 0
    kol_vo_zamen = 0
    len_array = len(array)
    for i in range(len_array):
        for j in range(0, len_array - 1 - i):
            kol_vo_sravneniy += 1
            if array[j] > array[j + 1]:
                kol_vo_zamen += 1
                array[j], array[j + 1] = array[j + 1], array[j]

n = int(input())
A = np.zeros(n,dtype=int)
li = [0,1,5]
for i in range(n):
    A[i] = li[randint(0,2)]
print(A)
bubbles_sort(A)
print(A)