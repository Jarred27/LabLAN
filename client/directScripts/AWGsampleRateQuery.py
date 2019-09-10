def function AWGsampleRateQuery()
	# AWGsampleRateQuery Summary of this function goes here
	# Detailed explanation goes here
	import query.py
	
	AWGadd = "TCPIP0::localhost::inst1::INSTR"
	Command = ":FREQ:RAST?"
	
	return = query(AWGadd,Command)