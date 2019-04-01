#!/usr/bin/env python

import socket


TCP_IP = '118.138.64.240'
TCP_PORT = 5005
BUFFER_SIZE = 1024
#MESSAGE = b'Hello, World!'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while 1:
    MESSAGE=bytes(input('CMD: '),'UTF8')
    if MESSAGE==b'quit':
        break
    errorFlag=s.connect_ex((TCP_IP, TCP_PORT))
    if errorFlag!=0:
        print("host not found, err#: "+str(errorFlag))
        continue
    s.send(MESSAGE)
    while(1):
        data = s.recv(BUFFER_SIZE)
        if(data==b'END_OUTPUT'):
            break
        print(data)
    s.close()

