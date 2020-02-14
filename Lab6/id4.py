while True:
    try:
        t = int(input("Скiльки часу пройшло:"))
        z = t%6
        if z <= 3:
            print("green")
        elif z <=4:
            print("Yellow")
        elif z <= 6:
            print("Red")
    except Exception:
        print("Невірно введені данні!")
    print("Перезапустити програму?(Так\Ні)")
    p = input()
    if p.lower() == "ні":
        break