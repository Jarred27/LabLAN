def function AWGvolatgeSet(channel, voltage)
	# AWGvolatgeSet Summary of this function goes here
	# Detailed explanation goes here
	import write.py
	
	AWGadd = "TCPIP0::localhost::inst1::INSTR"
	Command = "VOLT" + str(channel) + " " + str(voltage)
	
	return = write(AWGadd,Command)