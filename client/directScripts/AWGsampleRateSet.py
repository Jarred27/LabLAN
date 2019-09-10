def function AWGsampleRateSet(frequency)
	# AWGsampleRateSet Summary of this function goes here
	# Detailed explanation goes here
	import write.py
	
	AWGadd = "TCPIP0::localhost::inst1::INSTR"
	Command = ":FREQ:RAST " + str(frequency)
	
	return = write(AWGadd,Command)