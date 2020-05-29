import io
a = open("f.txt", "r")
b = open("g.txt", "w")
for line in a:
    flag = True
    if int(line)>=1:
        for n in range(2,int(line)):
            if int(line) % n == 0:
                flag = False
                break;
        if flag:
            b.write(line)
a.close()
b.close()
print("в файл b були дописані прості числа")