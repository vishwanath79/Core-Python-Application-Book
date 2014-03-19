# 2-6 UDP Timestamp Server

from socket import *
from time import ctime
HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)
# dgram UDP socket type
udpSerSock = socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)
while True:
    print 'waiting for message...'
    data,addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto('[%s]%s'% (
        ctime(),data),addr)
    print'....reicieved from and returned to:', addr