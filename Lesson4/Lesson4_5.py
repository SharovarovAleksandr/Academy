def list_num1(str1): # Через функцію мах
    str1_m = str1.replace(" ", "")
    str2 = set(str1_m)
    col = dict()
    rez=[]
    for i in str2:
        col[i] = str1_m.count(i)
    n=max(col.values())
    for i in str2:
        if col[i]==n:
            rez+=i
    return rez,n

def list_num2(str1):  #Через цикл
    str1_m = str1.replace(" ", "")
    str2 = set(str1_m)
    col = dict()
    rez=[]
    n=1
    for i in str2:
        col[i] = str1_m.count(i)
        if col[i]>n:
            n=col[i]
    for i in str2:
        if col[i]==n:
            rez+=i
    return rez,n

str1="fkbv aljb wiuygweo ygc9bc yggci itffg utfsuTV IYFAFALksv sdc z ddddd cc rrrrrr qqqqqq"

rez,n= list_num1(str1)
print("Варіант 1:  Літера ",rez," зустрічається ",n," раз")
rez,n= list_num2(str1)
print("Варіант 2:  Літера ",rez," зустрічається ",n," раз")
