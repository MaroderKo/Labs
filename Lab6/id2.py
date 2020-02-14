from enum import Enum


class converter (Enum):
    USD = 1
    EUR = 2
    CZK = 3
    PLN = 4
x = float (input ( 'amount of money:'))
p = converter [input ( 'currency:')]
if p == converter.USD:
    print(x*24.58, "UAH")
elif p == converter.EUR:
    print(x * 26.82, "UAH")
elif p == converter.CZK:
    print(x * 1.07, "UAH")
elif p == converter.PLN:
    print(x * 6.29, "UAH")