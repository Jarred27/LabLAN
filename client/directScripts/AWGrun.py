def function AWGrun()
	# AWGRUN Summary of this function goes here
	# Detailed explanation goes here
	import write.py
	
	AWGadd = "TCPIP0::localhost::inst1::INSTR"
	Command = ":INIT:IMM"
	
	return = write(AWGadd,Command)