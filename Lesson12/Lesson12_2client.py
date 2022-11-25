# Програма запрашує у користувача два числа та передає їх на сервер для опрацювання
# Отримує від сервера 4 відповіді результатів арифметичних операцій з цими числами (+-/*)
# Для виявлення результати якої операції передаються від сервера, першим символом змінної стоїть знак операції
# Далі клієнт аналізує зміст отриманого повідомлення та друкує відповідь


import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))

while True:
    a=input(" Введіть число A (END для виходу)  ")
    sock.send(bytes(a, encoding='UTF-8'))
    if a=="END":
        break
    b=input(" Введіть число B ")
    sock.send(bytes(b, encoding='UTF-8'))
    st = time.time()

    for i in range(4):
        rez = sock.recv(1024)
        rez = rez.decode('utf-8')
        if rez[0]=="*":
            print("Добуток дорівнює -",rez[1:])
        elif rez[0]=="/":
            print("Результат ділення - ",rez[1:])
        elif rez[0]=="-":
            print("Різниця між числами - ",rez[1:])
        elif rez[0]=="+":
            print("Сума чисел - ",rez[1:])
        else:
            print("Отримав незрозумілу команду ",rez[0])
            break
    print("Час виконання операції сервером - ",time.time()-st)

sock.close()



