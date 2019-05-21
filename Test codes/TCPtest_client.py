#!/usr/bin/env python

import socket


TCP_IP = '118.138.64.240'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = b'Hello, World!'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
print('sending message')
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print ("received data:", data)
