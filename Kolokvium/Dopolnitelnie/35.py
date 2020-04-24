"""35. Дан лінійний масив цілих чисел. Перевірте, чи є він упорядкованим по
спаданню."""
A = list()
flag = True
for n in range(10):
    A.append(int(input()))
prev = A[0]
for n in range(1, len(A)):
    if A[n] <= prev:
        continue
    else:
        flag = False
        break
print("він"+(" не" if not flag else "")+" упорядкований по спаданню.")