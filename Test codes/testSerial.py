import serial
import io

## seting up serial connection
ser = serial.Serial()  # open serial port
ser.baudrate = 9600
ser.port = 'COM3'
ser.timeout=1
ser.open()
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser,1), encoding='ascii',newline='\r\n')#wrapper allows sio.readline() to return data correctly
print(ser.name)         # check which port was really used

## displaying content in buffer
print('starting')     # write a string
ser.write(b'\r\n') #prompts EDFA to return 'MSA::EDFA>' to verify its there
line=sio.readline()
print(line)
while line!='MSA::EDFA> ':#prints serial port data until the ready message is sent
    #print('test')
    #line=ser.readline(50)
    #print(line)
    line = sio.readline()
    if line!='':
        print(line)
print('Device found')

## issuing boot command
print ('rebooting')
ser.write(b'BOOT\r\n')#sio.write was returning a syntax error so this method should be used to send ctrl instructions
line=sio.readline()
print(line)
while line!='MSA::EDFA> ':
    #print('test')
    #line=ser.readline(50)
    #print(line)
    line = sio.readline()
    if line!='':
        print(line)

## exiting
print('stopping')
ser.close()             # close port