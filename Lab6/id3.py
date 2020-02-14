from enum import Enum


class month (Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12
class season (Enum):
    Winter = 1
    Spring = 2
    Summer = 3
    Autumn = 4
s = month [input ( 'month:')]
a = month(s).value
if a < 3:
    print(season.Winter.name)
elif a < 6:
    print(season.Spring.name)
elif a < 9:
    print(season.Summer.name)
elif a < 12:
    print(season.Autumn.name)
elif a == 12:
    print(season.Winter.name)