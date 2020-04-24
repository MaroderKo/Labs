"""38. Дані про направлення вітру (північний, південний, східний, західний) і
силі вітру за декаду листопада зберігаються в масиві. Визначити, скільки днів дув
південний вітер з силою, що перевищує 8 м / с."""
import random
A = list()
sum = 0
for n in range(10):
    nap = random.randint(0, 3)
    if nap == 0:
        A.append(["ПД", random.randint(0, 15)])
    elif nap == 1:
        A.append(["ПН", random.randint(0, 15)])
    elif nap == 2:
        A.append(["ЗХ", random.randint(0, 15)])
    elif nap == 3:
        A.append(["СХ", random.randint(0, 15)])
for n in A:
    if n[0] == "ПД" and n[1]>=8:
        sum+=1
print(sum)
