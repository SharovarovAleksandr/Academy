import threading
import time

def f(x):
    return x ** 0.5

def iter1(n):
    for j in range(0, 300000, 100000):
        mid = 0
        for k in range(n):
            start = time.time()
            for i in range(j):
                x = f(i)
            mid = mid + (time.time() - start)
        print("Кількість ітерацій iter1- ", j, "   Середній час виконання ", n, " проходів становить -", mid / n)

def iter2(n):
    for j in range(300000, 600000, 100000):
        mid = 0
        for k in range(n):
            start = time.time()
            for i in range(j):
                x = f(i)
            mid = mid + (time.time() - start)
        print("Кількість ітерацій iter2- ", j, "   Середній час виконання ", n, " проходів становить -", mid / n)

def iter3(n):
    for j in range(600000, 1000001, 100000):
        mid = 0
        for k in range(n):
            start = time.time()
            for i in range(j):
                x = f(i)
            mid = mid + (time.time() - start)
        print("Кількість ітерацій iter1- ", j, "   Середній час виконання ", n, " проходів становить -", mid / n)

t=time.time()
iter1(5)
iter2(5)
iter3(5)
tt1=time.time() - t
print("Загальний час виконання програми без threading",tt1)


t=time.time()
task1 = threading.Thread(target=iter1(5))
task2 = threading.Thread(target=iter2(5))
task3 = threading.Thread(target=iter3(5))
task1.start()
task2.start()
task3.start()
task1.join()
task2.join()
task3.join()
tt2=time.time() - t
print("Загальний час виконання програми з threading",tt2)
rez=(tt1-tt2)/tt1*100
print("Продуктивність підвищилася на ",rez," відсотків")