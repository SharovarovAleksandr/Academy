import os
def ofile1(vay):  #реалізаці алгоритму через зчитування всьго файлу у список
    if os.path.exists(vay):
         f=open(vay, "r", encoding="utf8")
    else:
        print("Такого файлу не існує")
        return 0
    str = list(f.read())
    n=len(str)
    j=0
    for i in range(n):
        if str[i]=="\n":
            j+=1
    return j

def ofile2(vay): #реалізаці алгоритму через зчитування файлу по строках
    if os.path.exists(vay):
         f=open(vay, "r", encoding="utf8")
    else:
        print("Такого файлу не існує")
        return 0
    j=1
    str = list(f.readline())
    if str==[]:
        print("Цей файл пустий або не містить тексту")
    while str!=[]:
        str = list(f.readline())
        j+=1
    return j-1

#n=input("Введіть путь до файлу : ")
n="name1"
print("У цьому файлі ",ofile1(n)," рядків")
print("У цьому файлі ",ofile2(n)," рядків")