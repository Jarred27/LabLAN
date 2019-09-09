def function AWGoutputQuery()
	# AWGoutputQuery Summary of this function goes here
	# Detailed explanation goes here
	import write.py
	
	AWGadd = "TCPIP0::localhost::inst1::INSTR"
	Command = "___"
	
	return = write(AWGadd,Command)