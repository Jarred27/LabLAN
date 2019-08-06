#!/usr/bin/env python

import socket


TCP_IP = '118.139.47.206'
TCP_PORT = 5005
BUFFER_SIZE = 1024
#MESSAGE = b'Hello, World!'


while 1:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('> ', end='')
    MESSAGE = bytes(input(), 'UTF8')
    if MESSAGE == b'quit':
        s.send(b'close_connection')
        break
    errorFlag = s.connect_ex((TCP_IP, TCP_PORT))
    if errorFlag != 0:
        print("host not found, err#: "+str(errorFlag))
        continue
    s.send(MESSAGE)
    while 1:
        data = s.recv(BUFFER_SIZE)
        if not data:
            break
        print(data.decode("utf-8"))

    s.close()

