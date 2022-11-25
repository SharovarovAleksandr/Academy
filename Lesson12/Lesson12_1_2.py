# Програма вираховує час необхідний для обчислення n кількості факторіалів рандомних чисел від 1 до 1000
# Використання методу ProcessPoolExecutor()

import time
import random
import concurrent.futures as pool

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

n=50
t1=ntime(n)
print("Time execution ",n," numbers is - ",t1)

if __name__ == '__main__':
    executor=pool.ProcessPoolExecutor()
    result=executor.submit(ntime,n)
    t3=result.result()
    print("Time execution ",n," numbers is - ",t3)
    rez2=(t1-t3)/t1*100
    print("Продуктивність ProcessPoolExecutor підвищилася на ",rez2," відсотків")
if rez2>0:
    print()
