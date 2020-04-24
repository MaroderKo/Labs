"""46. Задана таблиця назв товарів, що випускаються заводом. Визначте, чи
повторюється в цій таблиці назва першого товару, і, якщо повторюється, видаліть
назву першого товару з таблиці."""
A = list()
primer = ""
flag = True
gf = False
for n in range(3):
    A.append(input())
    if not flag:
        primer = A[n]
        flag = False
        continue
    if A[n] == primer:
        gf = True
if gf:
    while primer in A:
        A.remove(primer)
