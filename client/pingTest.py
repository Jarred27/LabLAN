import getConfigs
import socket
import sys

# when running this file it will run "__main__" section which will call pingTest() function
# to call external to python e.g. in matlab call > python pingTest arguments (there are no arguments required for pingTest)

def pingTest():
    #load settings
    [TCP_IP,TCP_PORT,BUFFER_SIZE,connectionTimeout]=getConfigs.getConfigs().split(", ")
    TCP_PORT=int(TCP_PORT)
    BUFFER_SIZE=int(BUFFER_SIZE)
    connectionTimeout = int(connectionTimeout)

    #define string to send
    messageString = "ping"
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
        returnString = data.decode("utf-8")

    s.close()
    return returnString

if __name__=="__main__":
    #arg1 = sys.argv[1]...
    result = "ping23"#pingTest()
    print(result)
    sys.exit(result.split(" ")[0] == "ping")
