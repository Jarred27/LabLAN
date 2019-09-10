def function AWGrefClockQuery()
	# AWGrefClockQuery Summary of this function goes here
	# Detailed explanation goes here
	import query.py
	
	AWGadd = "TCPIP0::localhost::inst1::INSTR"
	Command = ":ROSC:FREQ?"
	
	return = query(AWGadd,Command)