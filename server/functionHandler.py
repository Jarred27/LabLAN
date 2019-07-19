import socket
import pyvisa as visa
import numpy

#TCP_IP = '118.138.123.80' #this stuff is defined in the config file
#TCP_PORT = 5005
#BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

# global objects
rm = visa.ResourceManager() #visa object

def functionhandler(args):
    #print(args)
    if args[0]=="ping":
        print("ping")
        return "pong"
    if args[0]=="visa":
        if args[1]=="listDevices":
            return numpy.concatenate(rm.list_resources())
        if args[1]=="read":
            return
        if args[1]=="write":
            return
    return "err: unrecognised cmd"#return null for no response

def runTCP(TCP_IP,TCP_PORT,BUFFER_SIZE,filePath):
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
                    message = functionhandler(args.split(', '))# note that this makes ',' or ' ' by themselves not split,
                    # this is to add robustness but requires client progrm to use correct formatting
                except:
                    message = "err: command_error"
                    print("here")
                if message:#ignore if empty return
                    conn.send(bytes(message, 'UTF8'))
                conn.shutdown(1)
                conn.close()
    return#will never get here
