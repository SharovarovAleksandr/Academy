def fib(max,l=[0,1]):
    if max > (l[-1]+l[-2]) :
        l.append(l[-1] + l[-2])
        return fib(max)
    else:
        return l


n=int(input("Введить максимальне число для послідовності Фібоначі :"))
print(fib(n))
