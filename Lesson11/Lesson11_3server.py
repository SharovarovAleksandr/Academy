import socket

def str_operator(st):
    #st = "   Шла Саша   по шоссе  и сосала   сушку   "
    l = []
    n1 = n2 = 0
    for i in range(len(st)):
        if st[i] == " ":
            n1 += 1
        else:
            break
    for i in range(-1, -len(st), -1):
        if st[i] == " ":
            n2 += 1
        else:
            break
    for i in range(len(st)):
        if st[i] == " ":
            l.append(i)
    c = len(l) + 1
    for i in range(n1, len(l) - n2 - 1):
        if l[i] == l[i + 1] - 1:
            c = c - 1
    c = c - n1 - n2
    d = len(st) - len(l)
    return str(c),str(d)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 55000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
conn, addr = sock.accept()
while True:
    print('connected:', addr)
    try:
        a = conn.recv(1024)
        st = a.decode('utf-8')
        if a=="STOP":
            break
        b, c = str_operator(st)
        conn.send(bytes(b, encoding='utf-8'))
        conn.send(bytes(c, encoding='utf-8'))
    except ConnectionAbortedError:
        break
    else:
        continue
conn.close()
print("Робота сервера завершена по STOP.")

