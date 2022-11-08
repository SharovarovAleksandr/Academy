def rev(n): # через строчную переменную
    s=str(n)
    s1=""
    num=len(s)
    for i in range(num):
        s1 += s[(num-i-1)]
    return int(s1)

def rev1(n): # через индексирование
    s=str(n)
    l1=list(s)
    l2=list(s)
    s=""
    num=len(l1)
    for i in range(num):
        l2[i]=l1[(num-i-1)]
        s += str(l2[i])
    return int(s)

def rev2(n): #через метод append
    s=str(n)
    l1=list(s)
    l2=[]
    s=""
    num=len(l1)
    for i in range(num):
        l2.append(l1[(num-i-1)])
        s += str(l2[i])
    return int(s)

n=int(input("Введіть число : "))
print(rev(n))
print(rev1(n))
print(rev2(n))