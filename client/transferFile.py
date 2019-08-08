import getConfigs
import socket
import sys

#  moves file into dedicated folder on server, needs to be pushed onto AWG with uploadFile.py

def transferFile(filePath,destFilename):
    #load settings
    [TCP_IP,TCP_PORT,BUFFER_SIZE,connectionTimeout]=getConfigs.getConfigs().split(", ")
    TCP_PORT=int(TCP_PORT)
    BUFFER_SIZE=int(BUFFER_SIZE)
    connectionTimeout = int(connectionTimeout)

    s = socket.socket()
    s.connect((TCP_IP, TCP_PORT))
    s.send(bytes("file, txRequest, " + destFilename, "UTF8"))
    #print('waiting for server')
    response = s.recv(BUFFER_SIZE)
    if response != b'file, rxReady':
        #print("handshake error")
        #print(response.decode("utf-8"))
        return 1
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
    try:
        response = s.recv(BUFFER_SIZE)
        response=response.decode("utf-8")
        arr=response.split(", ")
        print(arr)
        errFlag=arr[2]
    except:
        errFlag=1
    #print("Exiting")
    s.close  # Close the socket when done
    return errFlag

if __name__=="__main__":
    if len(sys.argv) == 3:
        filePath = sys.argv[1]
        destFilename = sys.argv[2]
        print(transferFile(filePath,destFilename))#print 0 for success, 1 for error (error flag value)
    else:
        print("expected 2 arguments got "+str(len(sys.argv)-1))
