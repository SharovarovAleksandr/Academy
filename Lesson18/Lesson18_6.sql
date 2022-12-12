import mysql.connector

# mdb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Alevar")
#
# curs=mdb.cursor()
# curs.execute("CREATE DATABASE TestData ")
#
mdb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Alevar",
    database="TestData")
curs=mdb.cursor()
# curs.execute("CREATE TABLE Customer (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), address VARCHAR(255))")

name_list=['Peter','Amy', 'Hannah', 'Michael','Sandy','Betty','Richard','Susan','Vicky','Ben','William','Chuck','Viola']
address_list=[ 'Lowstreet 4','Apple st 652','Mountain 21','Valley 345','Ocean blvd 2','Green Grass 1','Sky st 331','One way 98','Yellow Garden 2','Park Lane 38','Central st 954','Main Road 989','Sideway 1633']
en="')"

comanda="select * FROM testdata.customer"

#comanda="delete FROM name WHERE name!=''"
#comanda= "INSERT INTO Testdata.Customer (name) VALUES (name_list())"

# for i in name_list:
#     comanda= "INSERT INTO Testdata.Customer (name) VALUES ('"+i+en
print(comanda)
#curs.execute(comanda)
#mdb.commit()

select * FROM testdata.customer;
# for i in name_list:
#     comanda= '"INSERT INTO Customer name VALUES '+i+en
#     curs.execute(comanda)
# for i in address_list:
#     comanda = 'INSERT INTO Customer address VALUES "' + i + en
#     curs.execute(comanda)
