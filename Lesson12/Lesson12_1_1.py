# Програма вираховує час необхідний для обчислення n кількості факторіалів рандомних чисел від 1 до 1000
# Використання методу ThreadPoolExecutor

import time
import random
import concurrent.futures

def fact(x):
    if x<0 or not isinstance(x,int):
        return print("Факторіал можливо вирахувати тільки з цілого позитивного числа. Перевірте вхідні данні. ")
    s=1
    for i in range(1,x+1):
        s=s*i
    return s

def ntime(n):
    st=time.time()
    for i in range(n):
        rd=random.randint(1,1000)
        print(fact(rd))
    return time.time()-st

n=5
t1=ntime(n)
print("Time execution ",n," numbers is - ",t1)


with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    future=executor.submit(ntime,n)
    t2=future.result()
    print("Time execution ",n," numbers is - ",t2)

rez1=(t1-t2)/t1*100
print("Продуктивність ThreadPoolExecutor підвищилася на ",rez1," відсотків")

