# Програма вираховує час необхідний для обчислення n кількості факторіалів рандомних чисел від 1 до 1000
# Використання двох методів ThreadPoolExecutor та ProcessPoolExecutor
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

n=8
rez1=0
rez2=0
t1=ntime(n)
print("Time execution ",n," numbers is - ",t1)

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    future=executor.submit(ntime,n)
    t2=future.result()
    print("Time execution ",n," numbers is - ",t2)
    executor.shutdown()
    rez1=(t1-t2)/t1*100

with concurrent.futures.ProcessPoolExecutor(max_workers=5) as pool:
    if __name__ == '__main__':
        result=pool.submit(ntime,n)
        t3=result.result()
        print("Time execution ",n," numbers is - ",t3)
        rez2=(t1-t3)/t1*100
    executor.shutdown()

# ПИТАННЯ ДО ВИКЛАДАЧА!
#Чому при використанні одночасно двох процессів у програмі вона працює некорректно,
# хоча були застосовані оператори  executor.shutdown()?
#Заздалегідь вдячний за відповідь.

print(" ThreadPoolExecutor ефективніший на ",rez1,"відсотків")
print("ProcessPoolExecutor ефективніший на ",rez2,"відсотків")
if rez1>rez2:
    print("Краще використовувати ThreadPoolExecutor  ")
else:
    print("Краще використовувати ProcessPoolExecutor ")
