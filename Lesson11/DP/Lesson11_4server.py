import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 55000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    a =conn.recv(1024)
    b= conn.recv(1024)
    c=str(int(a)+int(b))
    print(c)
    conn.send(bytes(c,encoding='utf-8'))
conn.close()