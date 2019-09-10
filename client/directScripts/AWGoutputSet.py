def function AWGoutputSet(channel, ONorOFF)
	# AWGoutputSet Summary of this function goes here
	# channel is which channel you want 
	# ONorOFF is either 1 or 0
	
	import write.py
	
	AWGadd = "TCPIP0::localhost::inst1::INSTR"
	Command = ":OUTP" + str(channel) + " " + str(ONorOFF)
	
	return = write(AWGadd,Command)