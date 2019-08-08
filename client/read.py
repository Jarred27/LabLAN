import getConfigs
import socket
import sys

# takes an input argument of the device to be read and returns a string containing "err [...]" or devices response

def read(instID):
    #load settings
    [TCP_IP,TCP_PORT,BUFFER_SIZE,connectionTimeout]=getConfigs.getConfigs().split(", ")
    TCP_PORT=int(TCP_PORT)
    BUFFER_SIZE=int(BUFFER_SIZE)
    connectionTimeout = int(connectionTimeout)

    #define string to send
    messageString = "visa, read, "+instID
    formattedMessage=bytes(messageString, 'UTF8')

    #bind port
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        return "err socketConfigError"

    #connect to server
    errorFlag = s.connect_ex((TCP_IP, TCP_PORT))
    if errorFlag != 0:
        returnString="err hostNotFoundErr#:"+str(errorFlag)
        s.close()
        return returnString

    #send message
    s.send(formattedMessage)
    data = s.recv(BUFFER_SIZE)
    if not data:
        returnString="err noResponse"
    else:
        response = data.decode("utf-8")
        arr = response.split(", ")
        if len(arr)<=3:
            returnString = "err invalidResponse"
        else:
            if arr[2]==1:#server returned error flag
                returnString = "err "+arr[3]
            else:
                i=3
                max=len(arr)
                returnString=""
                while 1:
                    returnString+=arr[i]
                    i+=1
                    if i>=max:
                        break
                    returnString+=", "

    s.close()
    return returnString

if __name__=="__main__":
    if len(sys.argv) == 2:
        instID = sys.argv[1]
        print(read(instID))
    else:
        print("expected 1 argument got "+str(len(sys.argv)-1))
