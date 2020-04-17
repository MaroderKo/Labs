import numpy as np
import timeit


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

def reversed_bubbles(array):
    global kol_vo_sravneniy
    global kol_vo_zamen
    kol_vo_sravneniy = 0
    kol_vo_zamen = 0
    len_array = len(array)
    for i in range(len_array):
        for j in range(0, len_array - 1 - i):
            kol_vo_sravneniy += 1
            if array[j] < array[j + 1]:
                kol_vo_zamen += 1
                array[j], array[j + 1] = array[j + 1], array[j]


def select_sort(array):
    global kol_vo_sravneniy
    global kol_vo_zamen
    kol_vo_sravneniy = 0
    kol_vo_zamen = 0
    len_array = len(array)
    for i in range(len_array - 1):
        min_index = i
        for j in range(i + 1, len_array - 1):
            kol_vo_sravneniy += 1
            if array[j] < array[min_index]:
                min_index = j
        kol_vo_zamen += 1
        array[i], array[min_index] = array[min_index], array[i]

def reversed_select_sort(array):
    global kol_vo_sravneniy
    global kol_vo_zamen
    kol_vo_sravneniy = 0
    kol_vo_zamen = 0
    len_array = len(array)
    for i in range(len_array - 1):
        min_index = i
        for j in range(i + 1, len_array - 1):
            kol_vo_sravneniy += 1
            if array[j] > array[min_index]:
                min_index = j
        kol_vo_zamen += 1
        array[i], array[min_index] = array[min_index], array[i]

def insertion_sort(array):
    global kol_vo_sravneniy
    global kol_vo_zamen
    kol_vo_sravneniy = 0
    kol_vo_zamen = 0
    len_array = len(array)
    for i in range(1, len_array):
        k = array[i]
        min_index = i - 1
        kol_vo_sravneniy += 1
        while min_index >= 0 and array[min_index] > k:
            kol_vo_zamen += 1
            array[min_index + 1] = array[min_index]
            min_index -= 1
        array[min_index + 1] = k


def reversed_insertion_sort(array):
    global kol_vo_sravneniy
    global kol_vo_zamen
    kol_vo_sravneniy = 0
    kol_vo_zamen = 0
    len_array = len(array)
    for i in range(1, len_array):
        k = array[i]
        min_index = i - 1
        kol_vo_sravneniy += 1
        while min_index >= 0 and array[min_index] < k:
            kol_vo_zamen += 1
            array[min_index + 1] = array[min_index]
            min_index -= 1
        array[min_index + 1] = k

def cocktail_sort(array):
    global kol_vo_sravneniy
    global kol_vo_zamen
    kol_vo_sravneniy = 0
    kol_vo_zamen = 0
    len_array = len(array)
    proverka_zameni = True
    for i in range(len_array // 2):
        proverka_zameni = False
        for j in range(i + 1, len_array - 1):
            kol_vo_sravneniy += 1
            if array[j] < array[j - 1]:
                kol_vo_zamen += 1
                array[j], array[j - 1] = array[j - 1], array[j]
                proverka_zameni = True
        if not proverka_zameni:
            break
        proverka_zameni = False
        for j in range(len(array) - i - 1, i, -1):
            kol_vo_sravneniy += 1
            if array[j] < array[j - 1]:
                kol_vo_zamen += 1
                array[j], array[j - 1] = array[j - 1], array[j]
                proverka_zameni = True
        if not proverka_zameni:
            break


def reversed_cocktail_sort(array):
    global kol_vo_sravneniy
    global kol_vo_zamen
    len_array = len(array)
    kol_vo_sravneniy = 0
    kol_vo_zamen = 0
    proverka_zameni = True
    for i in range(len_array // 2):
        proverka_zameni = False
        for j in range(i + 1, len_array - 1):
            kol_vo_sravneniy += 1
            if array[j] > array[j - 1]:
                kol_vo_zamen += 1
                array[j], array[j - 1] = array[j - 1], array[j]
                proverka_zameni = True
        if not proverka_zameni:
            break
        proverka_zameni = False
        for j in range(len(array) - i - 1, i, -1):
            kol_vo_sravneniy += 1
            if array[j] > array[j - 1]:
                kol_vo_zamen += 1
                array[j], array[j - 1] = array[j - 1], array[j]
                proverka_zameni = True
        if not proverka_zameni:
            break

def shell_sort(array):
    global kol_vo_sravneniy
    global kol_vo_zamen
    kol_vo_sravneniy = 0
    kol_vo_zamen = 0
    len_array = len(array)
    space = len_array // 2
    while space > 0:
        for i in range(space, len_array):
            t = array[i]
            j = i
            kol_vo_sravneniy += 1
            while j >= space and array[j - space] > t:
                kol_vo_zamen += 1
                array[j] = array[j - space]
                j -= space
            array[j] = t
        space //= 2


def reversed_shell_sort(array):
    global kol_vo_sravneniy
    global kol_vo_zamen
    kol_vo_sravneniy = 0
    kol_vo_zamen = 0
    len_array = len(array)
    space = len_array // 2
    while space > 0:
        for i in range(space, len_array):
            t = array[i]
            j = i
            kol_vo_sravneniy += 1
            while j >= space and array[j - space] < t:
                kol_vo_zamen += 1
                array[j] = array[j - space]
                j -= space
            array[j] = t
        space //= 2


def piramid(array, len_array, i):
    global kol_vo_sravneniy
    global kol_vo_zamen
    maximalnoe = i
    l = 2 * i + 1
    r = 2 * i + 2
    kol_vo_sravneniy += 1
    if l < len_array and array[i] < array[l]:
        maximalnoe = l
    kol_vo_sravneniy += 1
    if r < len_array and array[maximalnoe] < array[r]:
        maximalnoe = r
    if maximalnoe != i:
        kol_vo_zamen += 1
        array[i], array[maximalnoe] = array[maximalnoe], array[i]
        piramid(array, len_array, maximalnoe)


def piramid_sort(array):
    global kol_vo_sravneniy
    global kol_vo_zamen
    kol_vo_zamen = 0
    kol_vo_sravneniy = 0
    len_array = len(array)
    piramid(array, len_array, 0)
    for i in range(len_array, -1, -1):
        piramid(array, len_array, i)
    for i in range(len_array - 1, 0, -1):
        kol_vo_zamen += 1
        array[i], array[0] = array[0], array[i]
        piramid(array, i, 0)


def reversed_piramid(array, len_array, i):
    global kol_vo_sravneniy
    global kol_vo_zamen
    minimalnoe = i
    l = 2 * i + 1
    r = 2 * i + 2
    kol_vo_sravneniy += 1
    if l < len_array and array[l] < array[minimalnoe]:
        minimalnoe = l
    kol_vo_sravneniy += 1
    if r < len_array and array[r] < array[minimalnoe]:
        minimalnoe = r
    if minimalnoe != i:
        kol_vo_zamen += 1
        array[i], array[minimalnoe] = array[minimalnoe], array[i]
        reversed_piramid(array, len_array, minimalnoe)


def reversed_piramid_sort(array):
    global kol_vo_sravneniy
    global kol_vo_zamen
    kol_vo_zamen = 0
    kol_vo_sravneniy = 0
    len_array = len(array)
    for i in range(len_array // 2 - 1, -1, -1):
        reversed_piramid(array, len_array, i)
    for i in range(len_array - 1, -1, -1):
        kol_vo_zamen += 1
        array[0], array[i] = array[i], array[0]

        reversed_piramid(array, i, 0)

flag = input("Чтобы рандом ввёл за вас числа нажмите 'Enter'. Для ручного ввода ведите любое значение и нажмите 'Enter': ")

if flag == '':
    array = np.random.randint(-100000, 100000, 100000)
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

Vibor_varianta = input(
    'Выберите способ сортировки: \n 1.Пузырьковый \n 2.Выбором \n 3.Вставками \n 4.Коктельный \n 5.Шела \n 6.Пирамидальная сортировка \n')
if Vibor_varianta == '1':
    reverse_check = input('Выберие порядок сортировки: \n 1.Прямой \n 2.Обратный \n')
    if reverse_check == '1':
        bubbles_sort(array)
        name = 'Пузырьковая прямая сортировка: '
    else:
        reversed_bubbles(array)
        name = 'Пузырьковая обратная сортировка: '
elif Vibor_varianta == '2':
    reverse_check = input('Выберие порядок сортировки: \n 1.Прямой \n 2.Обратный \n')
    if reverse_check == '1':
        select_sort(array)
        name = 'Прямая сортировка выбором: '
    else:
        reversed_select_sort(array)
        name = 'Обратная сортировка выбором: '
elif Vibor_varianta == '3':
    reverse_check = input('Выберие порядок сортировки: \n 1.Прямой \n 2.Обратный \n')
    if reverse_check == '1':
        insertion_sort(array)
        name = 'Прямая сортировка вставками: '
    else:
        reversed_insertion_sort(array)
        name = 'Обратная сортировка вставками: '
elif Vibor_varianta == '4':
    reverse_check = input('Выберие порядок сортировки: \n 1.Прямой \n 2.Обратный \n')
    if reverse_check == '1':
        cocktail_sort(array)
        name = 'Коктельная прямая сортировка: '
    else:
        reversed_cocktail_sort(array)
        name = 'Коктельная обратная сортировка: '
elif Vibor_varianta == '5':
    reverse_check = input('Выберие порядок сортировки: \n 1.Прямой \n 2.Обратный \n')
    if reverse_check == '1':
        shell_sort(array)
        name = 'Прямая сортировка Шелла: '
    else:
        reversed_shell_sort(array)
        name = 'Обратная сортировка Шелла: '
elif Vibor_varianta == '6':
    reverse_check = input('Выберие порядок сортировки: \n 1.Прямой \n 2.Обратный \n')
    if reverse_check == '1':
        piramid_sort(array)
        name = 'Пирамидальная прямая сортировка: '
    else:
        reversed_piramid_sort(array)
        name = 'Пирамидальная обратная сортировка: '

len_array = len(array)
print(f'Сортированый масив: \n {array}')
print(name)
print(f'Было произведено {kol_vo_sravneniy} сравнений')
print(f'Было произведено {kol_vo_zamen} замен')