import mysql.connector

pas=input("Введіть пароль для доступу до бази даних :")
name_list=['Peter','Amy', 'Hannah', 'Michael','Sandy','Betty','Richard','Susan','Vicky','Ben','William','Chuck','Viola']
address_list=['Lowstreet 4','Apple st 652','Mountain 21','Valley 345','Ocean blvd 2','Green Grass 1','Sky st 331', 'One way 98', 'Yellow Garden 2','Park Lane 38','Central st 954','Main Road 989','Sideway 1633']

mdb=mysql.connector.connect(
    host="localhost",
    user="root",
    password=pas)
curs=mdb.cursor()
curs.execute("CREATE  DATABASE IF NOT EXISTS TestData")
mdb=mysql.connector.connect(
    host="localhost",
    user="root",
    password=pas,
    database='Testdata')
curs = mdb.cursor()
curs.execute("CREATE TABLE Customer (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), address VARCHAR(255))")
n = ""
if len(name_list)!=len(address_list):
    n = input('ЗВЕРНІТЬ УВАГУ кількість елементів у списках name та address відрізняються. Продовжувати? (Y/N) : ')
if n == "Y" or n == "":
    for i in range(len(name_list)):
        var = (name_list[i],address_list[i])
        comanda = "INSERT Testdata.Customer (name,address) VALUES (%s, %s)"
        curs.execute(comanda, var)
    mdb.commit()
    curs.execute("SELECT COUNT(name)  FROM Testdata.Customer")
    print("До таблиці було додано ", curs.fetchall(), " елеменів. ")
else:
    print(" Елементи не додані до таблиці! ")




