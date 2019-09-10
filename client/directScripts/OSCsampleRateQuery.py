def function OSCsampleRateQuery()
	# OSCsampleRateQuery Summary of this function goes here
	# Detailed explanation goes here
	import query.py
	
	OSCadd = "USB0::0x0957::0x9013::MY50270101::0::INSTR"
	Command = ":FREQ:RAST?"
	
	return = query(OSCadd,Command)