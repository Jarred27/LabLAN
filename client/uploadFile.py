import getConfigs
import socket
import sys

def uploadFile(filePath,destFilename):
    #load settings
    [TCP_IP,TCP_PORT,BUFFER_SIZE,connectionTimeout]=getConfigs.getConfigs().split(", ")
    TCP_PORT=int(TCP_PORT)
    BUFFER_SIZE=int(BUFFER_SIZE)
    connectionTimeout = int(connectionTimeout)

    s = socket.socket()
    s.connect((TCP_IP, TCP_PORT))
    s.send(bytes("file, txRequest, " + destFilename, "UTF8"))
    print('waiting for server')
    response = s.recv(BUFFER_SIZE)
    if response == b'file, rxReady':
        #print('server ready')
    else:
        #print("unexpected response:")
        #print(response.decode("utf-8"))
        raise Exception("handshake error")
    # s.send("Hello server!")
    file = open(filePath, 'rb')
    #print('Sending...')
    line = file.read(BUFFER_SIZE)
    while (line):
        #print('Sending...')
        s.send(line)
        line = file.read(BUFFER_SIZE)
    #print("Done Sending")
    file.close()
    # s.shutdown(0)
    response = s.recv(BUFFER_SIZE)
    print(response.decode("utf-8"))
    #print("Exiting")
    s.close  # Close the socket when done

if __name__=="__main__":
    filePath = sys.argv[1]
    destFilename = sys.argv[2]
    print(uploadFile(filePath,destFilename))