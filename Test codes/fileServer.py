#from https://stackoverflow.com/questions/27241804/sending-a-file-over-tcp-sockets-in-python

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
f = open('C:\\Users\\anton\\Documents\\FYP repository\\Remotomation\\Test codes\\files from bill\\testRCV.txt','wb')
s.listen(5)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    c.settimeout(5)
    print('Got connection from', addr)
    print("Receiving...")
    l = c.recv(1024)
    while (l):
        print("Receiving...")
        f.write(l)
        l = c.recv(1024)
    f.close()
    print("Done Receiving")
    #c.send('Thank you for connecting')
    c.close()                # Close the connection