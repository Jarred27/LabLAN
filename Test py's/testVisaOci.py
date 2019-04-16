import pyvisa as visa
import time

instID='USB::0x0699::0x0368::C018240::INSTR'
rm=visa.ResourceManager()

avalialiableDevices=rm.list_resources()
if avalialiableDevices.__len__()==0:
    print('no avaliable devices ensure conected and drivers installed')
    exit(1)
i=0
while 1:
    if avalialiableDevices[i]==instID:
        print('device found')
        break
    if i == avalialiableDevices.__len__()-1:
        print('couldnt find matching device, exiting')
        print(avalialiableDevices)
        exit(1)
    i=i+1

inst=rm.open_resource(instID)
print(inst.query('*IDN?'))

inst.write('DAT:SOU CH2')
inst.write('DAT:ENC ASCI')
#time.sleep(1)
inst.write('DAT:STAR 1')
#time.sleep(2)
inst.write('DAT:STOP 200')
#time.sleep(1)
inst.write('CURV?')

print(inst.read())

exit(0)