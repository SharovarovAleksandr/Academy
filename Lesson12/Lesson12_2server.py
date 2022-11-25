# Сервер отримує від клієнта два числа та за допомогою чотирьох функцій виконує операції (+-*/)
# повертає клієнту 4 значення першим символом у коді возврату є символ операції
# якщо клієнт присилає команду END сервер закінчує роботу


#  ПИТАННЯ ЛЕКТОРУ!
# Чому, якщо, не ставити мінімальні затримки time.sleep(0.1) при виконанні функцій серсер та кліент працюють із помилками?
# Заздалегідь вдячний за відповідь.

import socket
import time

def add(a,b):
    c="+"+str(a+b)
    print(c)
    time.sleep(0.1)
    conn.send(bytes(c, encoding='utf-8'))
    return c

def mult(a,b):
    c ="*"+str(a * b)
    print(c)
    time.sleep(0.1)
    conn.send(bytes(c, encoding='utf-8'))
    return c

def div(a,b):
    c ="/"+str(a/b)
    print(c)
    time.sleep(0.1)
    conn.send(bytes(c, encoding='utf-8'))
    return c

def subs(a,b):
    c="-"+str(a-b)
    print(c)
    time.sleep(0.1)
    conn.send(bytes(c, encoding='utf-8'))
    return c

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 55000))
sock.listen(3)
print('Server is running, please, press ctrl+c to stop')
conn, addr = sock.accept()
print('connected:', addr)

while True:
    a = conn.recv(1024)
    a = a.decode('utf-8')
    if a=="END":
        break
    a=float(a)
    b = conn.recv(1024)
    b = float(b.decode('utf-8'))
    add(a, b)
    subs(a, b)
    mult(a, b)
    div(a, b)

conn.close()


