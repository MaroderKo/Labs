"""45. Перетин даху має форму півкола з радіусом R м. Сформувати таблицю,
яка містить довжини опор, які встановлюються через кожні R / 5 м."""
import math
R = int(input('Input Radius: '))
a = R / 5
b = 0
num = 0
while b < (2 * R - a):
    b += a
    num += 1
    print(f'Opora #{num} = {math.sqrt(b * (2 * R - b))} m')