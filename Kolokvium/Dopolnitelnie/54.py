"""54. Введіть масив з 20 елементів і визначте, чи є в ньому елементи з
однаковими значеннями."""
from random import  randint
A = list()
s = set()
for n in range(20):
    A.append(randint(-30,30))
for n in range(len(A)):
    s.add(A[n])
if len(s) == len(A):
    print("Povtorov net")
else:
    print("Povtori est'")