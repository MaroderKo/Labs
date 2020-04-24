"""37. Розсортуйте заданий лінійний масив по зростанню."""
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

import numpy as np
flag = input("Чтобы рандом ввёл за вас числа нажмите 'Enter'. Для ручного ввода ведите любое значение и нажмите 'Enter': ")

if flag == '':
    array = np.random.randint(-100, 100, 100)
else:
    print("Для выхода из режима ввода нажмите 'Enter'")
    while True:
        try:
            array = []
            for i in range(30):

                a = int(input(f'Введите {i + 1} елемент: '))
                array.append(a)

            break
        except ValueError:
            break
if len(array) == 0:
    exit()

print(f'Не сортированый массив: \n {array}')
bubbles_sort(array)
print(f'Cортированый массив: \n {array}')