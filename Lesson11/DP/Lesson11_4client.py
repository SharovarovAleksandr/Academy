import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))
a=input("Введіть число а: ")
b=input("Введіть число b: ")
sock.send(bytes(a, encoding='UTF-8'))
sock.send(bytes(b, encoding='UTF-8'))
print("Числа відправлені")
data = sock.recv(1024)
sock.close()
c=data.decode('utf-8')
print("Сума чисел дорівнює : ",c)
