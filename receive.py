import socket, sys

socket.setdefaulttimeout(150)
host = ''
port = 50005
socksize = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
print("Server started on port: {}".format(port))
s.listen(1)
conn, addr = s.accept()
print('New connection from {}:{}'.format(addr[0], addr[1]))
print("Now listening...\n")
while True:
    data = conn.recv(socksize)
    if not data:
        break
    elif data == 'killsrv':
        conn.close()
        sys.exit()
    else:
       print(data)
