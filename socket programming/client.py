import socket
c=socket.socket()
c.connect(("localh1ost",9999))
a=input("Your name:")
c.send(bytes(a,'utf-8'))
print(c.recv(1024).decode())
c.close()