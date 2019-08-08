import socket
import pyvisa as visa

# global objects
rm = visa.ResourceManager() #visa object

def functionhandler(args,conn,BUFFER_SIZE,filePath):
    if args[0]=="ping":
        print("ping")
        return "pong"
    if args[0]=="visa":
        if args[1]=="listDevices":
            returnString ="visa, avaliable devices"
            deviceArray=rm.list_resources()
            if deviceArray=="":
                returnString+=", null"
            for device in deviceArray:
                returnString+=", "
                returnString+=device
            return returnString
        if args[1]=="write" or args[1]=="query":
            try:
                target=rm.open_resource(args[2])
            except:
                return "visa, writeResult, 1, device open error"
            try:
                # recombine all text after inital arguments into one string
                max=len(args)
                i=3
                message=""
                while 1:
                    message+=args[i]
                    i += 1
                    if i>=max:
                        break
                    message += ", "

                target.write(message)
            except:
                return "visa, writeResult, 1, inst write error"
            if args[1]=="write":#if query then keep target instrument open and return read result
                target.close()
                return "visa, writeResult, 0"
        if args[1]=="read" or args[1]=="query":
            if args[1]=="read":
                try:
                    target=rm.open_resource(args[2])
                except:
                    return "visa, readResult, 1, device open error"
            try:
                returnString="visa, readResult, 0, "+target.read()
                target.close()
                return returnString
            except:
                return "visa, readResult, 1, read error"
    if args[0]=="file":
        if args[1]=="txRequest":
            destFilename=args[2]
            #sizeMax=args[3]
            #currentSize=0
            #conn.settimeout(5) #if nothing is sent for 5 seconds the connection times out and the file is assumed sent
            conn.send(bytes("file, rxReady", 'UTF8'))
            file = open(filePath+destFilename, 'wb')
            print("writing file: "+destFilename)
            try:
                line = conn.recv(BUFFER_SIZE)
            except:
                print("error in file rx")
                return "file, writeResult, 1, file rx error"
            while line:
                try:
                    file.write(line)
                except:
                    print("error in file write")
                    return "file, writeResult, 1, file write error"
                try:
                    line=conn.recv(BUFFER_SIZE)
                    #currentSize += line.__len__()
                except:
                    #print(line.__len__())
                    file.write(line)
                    #currentSize += line.__len__()
                    break
            #if not currentSize==sizeMax:
            #    print("expected "+str(sizeMax)+" bytes, got "+str(currentSize)+" bytes")
            #    return "file, writeResult, 1, byte size mismatch"
            return "file, writeResult, 0"
        if args[1]=="upload":#
            targetID=args[3]
            try:
                target=rm.open_resource(targetID)
            except:
                return "file, uploadResult, 1, device open error"
            try:
                target.write()
            except:
                return "file, uploadResult, 1, inst write error"
            target.close()
            return "file, uploadResult, 0"
    return "err, unrecognised_cmd"#return null for no response

def runTCP(TCP_IP,TCP_PORT,BUFFER_SIZE,filePath,connectionTimeout):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP object
        s.bind((TCP_IP, TCP_PORT))
    except:
        print("failed to bind port, check IP settings")
        input('press enter to exit')
        return
    while 1:
        print('waiting for connection')
        s.listen(1)
        try:
            conn, addr = s.accept()
            conn.settimeout(connectionTimeout)
            print ('Connection address:', addr)
        except:
            continue
        while 1:
            try:
                data = conn.recv(BUFFER_SIZE)
            except:
                print("conection lost, ip: ",addr)
                conn.close()
                break
            if data:
                print ("received data:", data)
                args = data.decode("utf-8")
                #print(args)
                try:
                    message = functionhandler(args.split(', '),conn,BUFFER_SIZE,filePath)# note that this makes ',' or ' ' by themselves not split,
                    # this is to add robustness but requires client progrm to use correct formatting
                except:
                    message = "err, command_error"
                    print("cmd err")
                if message:#ignore if empty return
                    try:
                        conn.send(bytes(message, 'UTF8'))
                    except:
                        print("send response error")
                conn.shutdown(1)
                conn.close()
    return#will never get here
