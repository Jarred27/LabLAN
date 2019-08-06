import getConfigs
import socket

def pingTest():
    #load settings
    [TCP_IP,TCP_PORT,BUFFER_SIZE]=getConfigs.getConfigs().split(", ")

    #define string to send
    messageString = "ping"
    formattedMessage=bytes(messageString, 'UTF8')

    #bind port
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        return "socketConfigError"

    #connect to server
    errorFlag = s.connect_ex((TCP_IP, TCP_PORT))
    if errorFlag != 0:
        returnString="hostNotFound,err#:"+str(errorFlag)
        s.close()
        return returnString

    #send message
    s.send(formattedMessage)
    while 1:
        data = s.recv(BUFFER_SIZE)
        if not data:
            returnString="no response"
            break
        returnString = data.decode("utf-8")

    s.close()
    return returnString

if __name__=="__main__":
    print(pingTest())
