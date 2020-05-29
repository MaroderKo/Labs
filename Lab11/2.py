a = open("old.txt", "r")
b = open("new.txt", "at")
l = "QWERTYUIOPASDFGHJKLZXCVBNM"
l1 = ""
rez = ""
for line in a:
    for t in line:
        if t in l:
            if not t in l1:
                l1+=t
for n in list(l):
    if not n in list(l1):
        rez+=str(n)
rez = str(rez)
b.write("\n")
b.write(rez)
a.close()
b.close()
print("В файл булодописано такий рядок: "+rez)