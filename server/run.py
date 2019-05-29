import functionHandler

configFile = open("config.txt", "r")
configs= configFile.read().split('\n')

for line in configs:
    [setting,value]=line.split()
    if setting=='TCP_IP':
        TCP_IP=value
        continue
    if setting=='TCP_PORT':
        TCP_PORT=int(value)
        continue
    if setting=='BUFFER_SIZE':
        BUFFER_SIZE=int(value)
        continue

functionHandler.runTCP(TCP_IP,TCP_PORT,BUFFER_SIZE)