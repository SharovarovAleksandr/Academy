#Fibo
a1=0
a2=1
i=2
n=int(input("Сколько елементов последовательности Фибоначи вы хотите сгенерировать? "))
if n>=1 :
    print("1 -й =",a1)
else: print(" Не может быть такой последовательности ")
if n>=2 :
    print("2 -й =",a2)
if n>=3 :
    while True:
        if i>=n : break
        a3=a1+a2
        a1=a2
        a2=a3
        i=i+1
        print(i,"-й =",a3)
