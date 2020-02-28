while True:
    try:
        a = set(map(str,"казка"))
        b = input()

        b1 = b[:list(b).index("!")]
        for t in b1:
            if t in a:
                a.remove(t)
        if len(a) == 0:
            print("Мiстить")
        else:
            print("Не мiстить")
    except Exception:
        print("Невірно введені данні!")
    print("Перезапустити програму?(Так\Ні)")
    p = input()
    if p.lower() == "ні":
        break