import socket
import logging

logging.basicConfig(filename='server.log',level=logging.INFO, filemode='a', format='%(name)s -%(asctime)s - %(levelno)s -  %(message)s')
lg=logging.getLogger(name='Server')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 55000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
lg.warning('WARNING - File "server.log" used two program Client and Server ')
lg.info('Server started')

while True:
    conn, addr = sock.accept()
    lg.info(f'Server get address {str(addr)}')
    conn.send(bytes("Готовий до работи.", encoding='utf-8'))
    conn.send(bytes(str(addr), encoding='utf-8'))
    lg.info(f'Server send address {str(addr)}')
    a = conn.recv(1024)
    a = a.decode('utf-8')
    lg.info(f'Server get response from Client {a}')
    if a==str(addr):
        print("Адреси співпадають")
        d=input("Для завершення роботи введіть * ")
        conn.send(bytes(d, encoding='utf-8'))
        lg.info('Server successful ended of work ')
        break
    else:
        lg.error('ERROR - Address Server and Client are different ')
        break
conn.close()

print("Робота сервера закінчена.")