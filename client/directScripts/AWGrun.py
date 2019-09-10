def function AWGrun()
	# AWGrun sets the run state
	
	import write.py
	
	AWGadd = "TCPIP0::localhost::inst1::INSTR"
	Command = ":INIT:IMM"
	
	return = write(AWGadd,Command)