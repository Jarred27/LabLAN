import socket

TCP_IP = '118.138.123.80'
TCP_PORT = 5005
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))


def functionhandler(args):
    print(args)
    if args[0]=="test":
        print("yay")
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
            functionhandler(args.split())
