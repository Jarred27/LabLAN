def function AWGrefClockQuery()
	# AWGrefClockQuery Summary of this function goes here
	# Detailed explanation goes here
	import write.py
	
	AWGadd = "TCPIP0::localhost::inst1::INSTR"
	Command = ":ROSC:FREQ?"
	
	return = write(AWGadd,Command)