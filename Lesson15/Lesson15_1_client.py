import socket
import logging

logging.basicConfig(filename='server.log',level=logging.INFO, filemode='a', format='%(name)s -%(asctime)s - %(levelno)s - %(message)s')
lg=logging.getLogger(name='Client')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))
lg.info('Client started')

while True:
    a = sock.recv(1024)
    a = a.decode('utf-8')
    lg.info(f'Client get message from Server - {a}')
    print(a)
    a = sock.recv(1024)
    a = a.decode('utf-8')
    lg.info(f'Client get address from Server {a}')
    print("Адресу запам'ятав ", a)
    sock.send(bytes(a, encoding='UTF-8'))
    lg.info(f'Client send address to Server {a}')
    print("Дивись роботу серверу!")
    b = sock.recv(1024)
    b = b.decode('utf-8')
    if b=="*":
        lg.info('Client ended work successful')
        break
    else:
        lg.error(f'Error - I wait response Server "*" but get command "{b}" ')
        lg.info('Client ended work with ERROR! ')
        break
sock.close()
