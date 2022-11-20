import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))

while True:
    a = sock.recv(1024)
    a = a.decode('utf-8')
    print(a)
    a = sock.recv(1024)
    a = a.decode('utf-8')
    print("Адресу запам'ятав ", a)
    sock.send(bytes(a, encoding='UTF-8'))
    b = sock.recv(1024)
    b = b.decode('utf-8')
    if b=="*":
        break
sock.close()
