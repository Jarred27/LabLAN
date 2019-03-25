#!/usr/bin/env python

import socket


TCP_IP = '192.168.1.200'
TCP_PORT = 5005
BUFFER_SIZE = 1024
#MESSAGE = b'Hello, World!'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while 1:
    MESSAGE=bytes(input(),'UTF8')
    if MESSAGE==b'quit':
        break
    s.connect((TCP_IP, TCP_PORT))
    print('sending message')
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    s.close()

    print ("received data:", data)