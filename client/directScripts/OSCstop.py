def function OSCrun()
	# OSCrun Summary of this function goes here
	# Detailed explanation goes here
	import write.py
	
	OSCadd = "USB0::0x0957::0x9013::MY50270101::0::INSTR"
	Command = ":INIT:IMM"
	
	return = write(OSCadd,Command)