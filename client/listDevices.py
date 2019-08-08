import getConfigs
import socket
import sys

# gets the server to return a list of avaliable instruments, no input arguments returns a string of addresses separated by ", "

def listDevices():
    #load settings
    [TCP_IP,TCP_PORT,BUFFER_SIZE,connectionTimeout]=getConfigs.getConfigs().split(", ")
    TCP_PORT=int(TCP_PORT)
    BUFFER_SIZE=int(BUFFER_SIZE)
    connectionTimeout = int(connectionTimeout)

    #define string to send
    messageString = "visa, listDevices"
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
        arr=response.split(", ")
        if len(arr)<=2:
            return "err invalidResponse"
        i=2
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
    #if len(sys.argv) == ...:
    #arg1 = sys.argv[1]...
    #else:
    result = listDevices()
    print(result)
    sys.exit(result.split(" ")[0] == "err")
