#from https://stackoverflow.com/questions/27241804/sending-a-file-over-tcp-sockets-in-python

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 5005              # Reserve a port for your service.

filepath="C:\\Users\\anton\\Documents\\FYP repository\\Remotomation\\Test codes\\files from bill\\"+"RRC_PM16QAM_22Gbd_1_sc_92Gsaps_imag_y.txt"
bufferSize=1024
#fileSize=os.path.getsize(filepath)
destFilename="testFile.txt"

s.connect((host, port))
s.send(bytes("file, txRequest, "+destFilename,"UTF8"))
print('waiting for server')
response=s.recv(bufferSize)
if response==b'file, rxReady':
    print('server ready')
else:
    print("unexpected response:")
    print(response.decode("utf-8"))
    raise Exception("handshake error")
#s.send("Hello server!")
file = open(filepath,'rb')
print('Sending...')
line = file.read(bufferSize)
while (line):
    print('Sending...')
    s.send(line)
    line = file.read(bufferSize)
print("Done Sending")
file.close()
#s.shutdown(0)
response=s.recv(bufferSize)
print(response.decode("utf-8"))
print("Exiting")
s.close                     # Close the socket when done