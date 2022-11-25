# Сервер отримує від клієнта два числа та за допомогою чотирьох async функцій виконує операції (+-*/)
# повертає клієнту 4 значення першим символом у коді возврату є символ операції
# якщо клієнт присилає команду END сервер закінчує роботу


#  ПИТАННЯ ЛЕКТОРУ!
# Програма працює коректно тільки перший раз, при спробі повторного введення даних стабільно викликається помилка
# if rez[0]=="*":   IndexError: string index out of range
# що свідчить про збої у процесі передачі даних на другій ітерації циклу. В чому проблема?
# Заздалегідь вдячний за відповідь.


import socket
import time
import asyncio

async def add(a,b):
    await asyncio.sleep(3)
    c="+"+str(a+b)
    print(c)
    #time.sleep(0.1)
    conn.send(bytes(c, encoding='utf-8'))
    return c

async def mult(a,b):
    await asyncio.sleep(1)
    c ="*"+str(a * b)
    print(c)
    #time.sleep(0.1)
    conn.send(bytes(c, encoding='utf-8'))
    return c

async def div(a,b):
    await asyncio.sleep(2)
    c ="/"+str(a/b)
    print(c)
    #time.sleep(0.1)
    conn.send(bytes(c, encoding='utf-8'))
    return c

async def subs(a,b):
    await asyncio.sleep(4)
    c="-"+str(a-b)
    print(c)
    #time.sleep(0.1)
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
    if __name__ =='__main__':
        ioloop = asyncio.get_event_loop()
        tasks = [
            ioloop.create_task(add(a,b)),
            ioloop.create_task(mult(a,b)),
            ioloop.create_task(subs(a,b)),
            ioloop.create_task(div(a,b)) ]
        ioloop.run_until_complete(asyncio.wait(tasks))
        ioloop.close()

conn.close()

