import socket

TCP_IP = '118.138.123.80'
TCP_PORT = 5005
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))

while 1:
	print('waiting for connection')
	s.listen(1)

	conn, addr = s.accept()
	print ('Connection address:', addr)
	
	
	
	while 1:
		try:
			data = conn.recv(BUFFER_SIZE)
		except:
			print("conection lost, ip: ",addr)
			break
		if data:
			print ("received data:", data)
			String[] args = data.split("\\s");
		
	print('left loop')
	conn.close()
	
def functionHadler(args):
	switch args[0]:
		case test:
			print("yay")