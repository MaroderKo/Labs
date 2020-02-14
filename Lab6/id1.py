days = range (1, 32)
mounths = range (1, 13)
years = range (1901, 2020)
d, m, y = int (input ( 'day:')), \
int (input ( 'mounth:')), \
int (input ( 'year:'))
while True:
    try:
        a = [5,7,10,12]
        b = [2,4,6,8,9,11] # -1=31
        d, m, y = int(input('day:')), \
                  int(input('mounth:')), \
                  int(input('year:'))
        m_i = m
        n_i = d
        y_i = y
        m = m_i
        n = n_i
        y = y_i
        if n == 1:

            if m in a:
                m-=1
                n = 30
            elif m in b:
                m-=1
                n = 31
            elif m == 1:
                y-=1
                m = 12
                n = 31
            elif m == 3:
                m = 2
                n = 28
        elif m > 12 or m < 1 or n > 31 or n < 1:
            raise Exception("Невірно введені данні!")
        else:
            n -= 1
        print("Було ", n, "-е число ", m, "-гo місяця ", y, "-го року")
        a = [1,3,5,7,8,10]
        b = [4,6,9,11]
        c = [2]
        m = m_i
        n = n_i
        y = y_i
        if n+1>31 and m==12:
            m = 1
            n = 1
            y+=1
        elif n+1>31 and m in a:
            m+=1
            n = 1
        elif n+1>30 and m in b:
            m += 1
            n = 1
        elif n+1>29 and m in c:
            m += 1
            n = 1
        else:
            n+=1
        print("Стане ", n, "-е число ", m, "-гo місяця ", y, "-го року")
    except Exception:
        print("Невірно введені данні!")
    print("Перезапустити програму?(Так\Ні)")
    p = input()
    if p.lower() == "ні":
        break