import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 55000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
conn, addr = sock.accept()
s={"name":'',"mail":'',"age":'',"gender":''}
while True:
    print('connected:', addr)

    conn.send(bytes("Давайте знайомитися як Вас звати? ", encoding='utf-8'))
    a = conn.recv(1024)
    s["name"] = a.decode('utf-8')
    conn.send(bytes("Введіть ваш e-mail: ", encoding='utf-8'))
    a = conn.recv(1024)
    s["mail"] = a.decode('utf-8')
    conn.send(bytes("Введіть ваш вік: ", encoding='utf-8'))
    a = conn.recv(1024)
    s["age"] = a.decode('utf-8')
    conn.send(bytes("Ваша стать: ", encoding='utf-8'))
    a = conn.recv(1024)
    s["gender"] = a.decode('utf-8')
    conn.send(bytes("*", encoding='utf-8'))
    break

conn.close()

print("Персональні данні.")
print(s)