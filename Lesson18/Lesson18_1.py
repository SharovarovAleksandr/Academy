import mysql.connector

pas=input("Введіть пароль для доступу до бази даних :")

mdb=mysql.connector.connect(
    host="localhost",
    user="root",
    password=pas)
curs=mdb.cursor()
curs.execute("CREATE  DATABASE IF NOT EXISTS My_first_db")
mdb=mysql.connector.connect(
    host="localhost",
    user="root",
    password=pas,
    database='My_first_db')
curs = mdb.cursor()
curs.execute("CREATE TABLE Student (id INT, name VARCHAR(255))")
curs.execute("CREATE TABLE Employee (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), salary INT)")
curs.execute("ALTER TABLE Student MODIFY COLUMN id INT PRIMARY KEY")

comand="INSERT My_first_db.Student (id,name) VALUES (%s, %s)"
var=(1,"Jonny")
curs.execute(comand,var)

comand="INSERT My_first_db.Employee(id,name,salary) VALUES (%s, %s, %s)"
var=(1,"Jonny",10000)
curs.execute(comand,var)
mdb.commit()
