import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 55000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')


while True:

    conn, addr = sock.accept()
    conn.send(bytes("Готовий до работи за адресою.", encoding='utf-8'))
    conn.send(bytes(str(addr), encoding='utf-8'))
    a = conn.recv(1024)
    a = a.decode('utf-8')

    if a==str(addr):
        print("Адреси співпадають")
        conn.send(bytes("*", encoding='utf-8'))
        break

conn.close()

print("Робота сервера закінчена.")
