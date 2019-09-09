def function AWGrefClockSet(frequency)
	# AWGrefClockSet Summary of this function goes here
	# Detailed explanation goes here
	import write.py
	
	AWGadd = "TCPIP0::localhost::inst1::INSTR"
	Command = :ROSC:FREQ " + num2str(frequency)
	
	return = write(AWGadd,Command)