def function AWGvoltageQuery(channel)
	# AWGvoltageQuery Summary of this function goes here
	# Detailed explanation goes here
	import query.py
	
	AWGadd = "TCPIP0::localhost::inst1::INSTR"
	Command = "VOLT" + str(channel) + "?"
	
	return = query(AWGadd,Command)