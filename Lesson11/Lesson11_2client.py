import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))

while True:
    a = sock.recv(1024)
    a = a.decode('utf-8')
    if a=="*":
        break
    print(a)
    a=input()
    try:
        sock.send(bytes(a, encoding='UTF-8'))
    except ConnectionAbortedError:
        break
    else:
        continue

sock.close()
