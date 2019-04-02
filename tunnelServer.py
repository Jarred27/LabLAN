import serial
import io
import socket

TCP_IP = '118.138.64.240'
TCP_PORT = 5005
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))

ser = serial.Serial()  # open serial port
ser.baudrate = 9600
ser.port = 'COM3'
ser.timeout=1
ser.open()
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser,1), encoding='ascii',newline='\r\n')#wrapper allows sio.readline() to return data correctly
identString='MSA::EDFA> '
#print(ser.name)         # check which port was really used

while 1:
    print('waiting for connection')
    s.listen(1) #sits here and waits for conection when idle

    conn, addr = s.accept()
    print ('Connection address:', addr)
    while 1:
        n=0
        while 1:
            line = sio.readline()
            if line != '':
                conn.send(bytes(line,'UTF8'))
                n=0
            else:
                n=n+1
                if n>3: #if 10 blank lines are recieved assume nothing there
                    conn.send(b'END_OUTPUT')
                    break
            if line == identString:
                conn.send(b'END_OUTPUT')
                break
        data = conn.recv(BUFFER_SIZE)
        print('data: ',data+b'\r\n')
        if data==b'close_connection':
            conn.close()
            break
        ser.write(data+b'\r\n')