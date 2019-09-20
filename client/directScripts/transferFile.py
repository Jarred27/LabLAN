import getConfigs
import socket
import sys

#  moves file into dedicated folder on server, needs to be pushed onto AWG with uploadFile.py

def transferFile(filePath,destFilename):
    #load settings
    [TCP_IP,TCP_PORT,BUFFER_SIZE,connectionTimeout,AWG_address]=getConfigs.getConfigs().split(", ")
    TCP_PORT=int(TCP_PORT)
    BUFFER_SIZE=int(BUFFER_SIZE)
    connectionTimeout = int(connectionTimeout)

    s = socket.socket()
	
    #connect to server
    errorFlag = s.connect_ex((TCP_IP, TCP_PORT))
    if errorFlag != 0:
        returnString="err hostNotFoundErr#:"+str(errorFlag)
        s.close()
        return returnString
    message="file, txRequest, "+destFilename
    s.send(message.encode('UTF8'))
    #print('waiting for server')
    response = s.recv(BUFFER_SIZE)
    if response != b'file, rxReady':
        #print("handshake error")
        #print(response.decode("utf-8"))
        s.close
        return "err handshake error"
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
        #print(arr)
        if arr[2]!="0":
            returnString=response#"err server returned error"
        else:
            returnString="success"
    except:
        returnString="err server response lost"
    #print("Exiting")
    s.close  # Close the socket when done
    return returnString

if __name__=="__main__":
    if len(sys.argv) == 3:
        filePath = sys.argv[1]
        destFilename = sys.argv[2]
        result = transferFile(filePath,destFilename)
        print(result)
        sys.exit(result.split(" ")[0]=="err")
    else:
        print("expected 2 arguments got "+str(len(sys.argv)-1)+"\ncorrect usage: transferFile.py filePath destFilename")
        sys.exit(1)
