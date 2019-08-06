import socket

def getConfigs():
    #setting default settings
    TCP_IP=str(socket.gethostname())
    TCP_PORT="5005"
    BUFFER_SIZE="1024"

    #load settings from file
    configFile = open("config.txt", "r")
    configs = configFile.read().split('\n')
    for line in configs:
        [setting, value] = line.split(': ')
        if setting == 'TCP_IP':
            TCP_IP = value
            continue
        if setting == 'TCP_PORT':
            TCP_PORT = value
            continue
        if setting == 'BUFFER_SIZE':
            BUFFER_SIZE = value
            continue

    #put settings in a string to return
    returnString=TCP_IP+", "+TCP_PORT+", "+BUFFER_SIZE
    return returnString
        #to use in other finctions use:
        #import getConfigs
        #[TCP_IP,TCP_PORT,BUFFER_SIZE]=getConfigs.getConfigs().split(", ")
