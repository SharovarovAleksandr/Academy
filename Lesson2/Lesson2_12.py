import datetime
dat=input("Введите дату рождения (формат ДД.MM.ГГГГ) ")
db=int(dat[0:2])
mb=int(dat[3:5])
yb=int(dat[6:10])

curdat=datetime.datetime.now()
d=curdat.day
m=curdat.month
y=curdat.year
rez=(y-yb-1)*12+(m-1)+(12-mb)

print("Вы прожили" ,rez," полных месяцев")
