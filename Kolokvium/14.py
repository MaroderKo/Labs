"""14. Сформуйте лінійний масив дійсних чисел, елементи якого є відстанями,
пройденими тілом при вільному падінні на землю за 1, 2, ..., 10 с."""
A = []
g = 10
sum = 0
v0 = float(input("Введiть початкову шв предмета:"))
# Выставление начальных значений
for n in range(10):
    sum+=(v0+g)
    A.append(sum)
    v0=v0+g
# Подсчёт по формуле
print(A)