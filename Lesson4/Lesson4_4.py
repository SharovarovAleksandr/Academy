def variant1(a):  # через текстову змінну
    n=len(str(a))
    b=str(a)
    s=0
    for i in range(0,n):
        s+=int(b[i])
    return s

def variant2(a):  # через список
    b=list(str(a))
    s=0
    for i in b:
        s=s+int(i)
    return s

def variant3(a):  # через ділення
    s=0
    if a<10 :
        return a
    while True:
        x=a//10
        s+=a%10
        a=x
        if x<1 :
            return s


a=int(input("Введіть число:"))
print(variant1(a))
print(variant2(a))
print(variant3(a))




