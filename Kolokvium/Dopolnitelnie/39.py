"""39. Дані про температуру повітря і кількості опадів за декаду квітня
зберігаються в масивах. Визначити кількість опадів, що випали у вигляді дощу і у
вигляді снігу за цю декаду."""
import random
A = list()
rain = 0
snow = 0
for n in range(10):
    nap = random.randint(0, 1)
    if nap == 1:
        A.append([True, random.randint(-30,30)])
    if nap == 1:
        A.append([False, random.randint(-30,30)])
for n in A:
    if n[0] == True:
        if n[1] >-3:
            rain+=1
        else:
            snow+=1
print("Rain:"+str(rain))
print("Snow:"+str(snow))