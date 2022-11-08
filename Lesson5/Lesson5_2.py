def di(name,dict):
    f=open(name,"wt",encoding="utf8")
    for i in dict.keys():
        f.write(i)
        f.write(" : ")
        f.write(str(dict[i]))
        f.write("\n")
    f.close()

my_dic={"name1":10,
        "name2":20,
        "name3":30,
        "name4":40,
        "name5":50}

n=str(input("Введіть ключове значення: "))
if n in my_dic.keys():
    di(n,my_dic)
    print("Файл ",n," створено")
else:
    print("Такого ключового значення не має у словнику")

