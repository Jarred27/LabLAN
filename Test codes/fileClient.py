#from https://stackoverflow.com/questions/27241804/sending-a-file-over-tcp-sockets-in-python

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.

s.connect((host, port))
#s.send("Hello server!")
f = open('testFile.txt','rb')
print('Sending...')
l = f.read(1024)
while (l):
    print('Sending...')
    s.send(l)
    l = f.read(1024)
f.close()
s.shutdown()
print("Done Sending")
print(s.recv(1024))
s.close                     # Close the socket when done