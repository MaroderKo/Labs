while True:
        Tovar = dict()
        while True:
            print("Внесiть новий товар у список(формат - \"Назва Виробник Рiк_виробництва Кiлькiсть Цiна\"  ")
            print("Для виходу введiть знак \" ! \"")
            add_i = input()
            if add_i == "!":
                break
            list_i = list(map(str,add_i.split(" ")))
            if list_i[0] in dict(Tovar).keys():
                g = list(Tovar.get(list_i[0]))
                g.append(add_i)
                Tovar[list_i[0]] = g
            else:
                a = (add_i, "First")
                a = list(a)
                a.remove("First")
                Tovar[(list_i[0])] = a
        sum1 = 0
        for y in sorted(Tovar.keys()):
            for n in range(len(Tovar.get(y))):
                print(Tovar[y][n])

        print("Перезапустити програму?(Так\Ні)")
        p = input()
        if p.lower() == "ні":
            break