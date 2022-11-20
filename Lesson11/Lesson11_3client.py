import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))
a=""
while True:
    print("Напишіть речення а я підрахую скільки слів та букв у цьому реченні (якщо втомилися наберіть STOP для зупинки сервера) ")
    a=input()
    try:
        if a=="STOP":
            break
    except ConnectionAbortedError:
        print("Завершили роботу по команді STOP ")
        break
    else:
        sock.send(bytes(a, encoding='UTF-8'))
        data1 = sock.recv(1024)
        data2 = sock.recv(1024)
        b = data1.decode('utf-8')
        c = data2.decode('utf-8')
        print("У реченні ",b,"слів та ",c,"букв")

sock.close()


