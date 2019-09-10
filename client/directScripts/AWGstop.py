def function AWGstop()
	# AWGstop Summary of this function goes here
	# Detailed explanation goes here
	import write.py
	
	AWGadd = "TCPIP0::localhost::inst1::INSTR"
	Command = ":ABOR"
	
	return = write(AWGadd,Command)