import socket

sock = socket.socket()
sock.bind(('localhost', 7777))
sock.listen(1)
conn, addr = sock.accept()
while True:
    data = conn.recv(1024)
    if not data:
        # break
        pass
    if data:
        conn.send(input().encode())


conn.close()
