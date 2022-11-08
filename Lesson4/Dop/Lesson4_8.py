def rec(a):
    a+=1
    print(a)
    if a==100:
        print("Рекурсія закінчена ")
        return
    else:
        rec(a)

n=int(input("Введите целое число меньше 100 : "))
rec(n)

