nam=input("Enter new file name: ")
f=open(nam,"wt",encoding="utf8")
for i in range(1,101):
    if i%5==0:
        f.write(str(i))
        f.write("\n")
