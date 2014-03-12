# Create a TCP server that accepts messages from clients and returns them with timestamp prefix

#Import socket attributes
from socket import *
from time import ctime
HOST = '' # Indication to bind method so it can use any avail addr
PORT = 21567 # Random port number
BUFSIZ = 1024
ADDR = (HOST,PORT)
tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5) # Max # of incoming connections before refusals
while True:
    print 'Waiting for connection'
    tcpCliSock,addr = tcpSerSock.accept() 
    print '...connected from: ', addr
    # Wait for data
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break #break and close connection if message is blank
        tcpCliSock.send('[%s] %s' %(ctime(),data)) # Prepend time stamp
        tcpCliSock.close()
    tcpSerSock.close() #close socket
