def function AWGoutputQuery(channel)
	# AWGoutputQuery Summary of this function goes here
	# Channel is which you want
	import query.py
	
	AWGadd = "TCPIP0::localhost::inst1::INSTR"
	Command = ":OUTP" + str(channel) + "?"
	
	return = query(AWGadd,Command)