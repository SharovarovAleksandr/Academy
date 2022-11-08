import os
p=os.getcwd()+"\\"
list=os.listdir(p)
if list!=[]:
    k=0
    l=0
    for i in list:
       if os.path.isfile(p+i):
            print(i)
            l+=1
       else:
            print("|",i)
            k+=1
    print("У каталозі ",k," підкаталогів та ",l," файлів")
else:
    print("У цьому каталозі",p,"немає файлів та підкаталогів")