import pyvisa as visa

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
    if i == avalialiableDevices.__len__():
        print('couldnt find matching device exiting')
        exit(1)
    i=i+1

instrument=rm.open_resource(instID)
print(instrument.query('*IDN?'))

exit(0)