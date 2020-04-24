"""50. У лотереї розігрувалося 100 квитків. Таблиця містить 10 номерів
виграшних квитків. Перевірте, чи є квиток з номером N виграшним."""
import random
A = set()
N = int(input())
while len(A) < 10:
    A.add(random.randint(1,100))
if N in A:
    print("true")
else:
    print("false")