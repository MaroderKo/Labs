"""
3. Сформувати функцію для переведення натурального числа з десяткової системи
числення у шістнадцятирічну.
Виконав: Перепелиця А.С.
"""
from datetime import datetime
hex_list = "0123456789ABCDEF" # словарь шестрандатиричной системы исчисления
n = int(input('Введите число которое нужно преобразовать: '))
rez = ''  # Начальная пустая строка для заполнения
start_time = datetime.now()#Начало записи аремени
if n == 0:  # ноль-проверка
    k = 0
while n != 0:  # До ноля будет соеденять строки
    rez += hex_list[n % 16] #Заполнение строки ответов
    n = n // 16
k = rez[::-1] if rez != "" else k  # Для правильного отображения необходимо развернуть
print(k) # вывод результата
print(datetime.now() - start_time) #Вывод времени