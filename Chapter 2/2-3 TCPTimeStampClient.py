# 2-3 TCP Timestamp Client
from socket import *
# Server Host and Port
HOST = 'localhost'
PORT = 21567
BUFSIZ =1024
ADDR = (HOST,PORT)
#Allocate client socket and connect to server
tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

# Unlike Server loop, client loop exits when no user input or if if server quits
while True:
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data
    
tcp.CliSock.close()
    
