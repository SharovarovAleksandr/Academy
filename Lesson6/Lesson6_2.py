def inr(a):
    if a==0:
        return
    a-=1
    print(a)
    inr(a)

n=int(input("Введіть число : "))
inr(n)
