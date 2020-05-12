"""
2. Сформувати функцію, що визначатиме чи є задане натуральне число простим.
Простим називається число, що більше за 1 та не має інших дільників, окрім 1 та самого
себе).
Виконав: Перепелиця А.С.
"""
from datetime import datetime
def do(a, b = 2):
    global flag
    if b < a:
        if a%b == 0:
            flag = False
        else:
            do(a,b+1)


a = int(input()) # ввод начальных значений значений
flag = True
start_time = datetime.now()#Начало записи аремени
do(a) #Вызов функции
print(flag) # вывод результата
print(datetime.now() - start_time) #Вывод времени
