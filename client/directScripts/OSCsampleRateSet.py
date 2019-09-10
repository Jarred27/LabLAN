def function OSCsampleRateSet(frequency)
	# OSCsampleRateSet Summary of this function goes here
	# Detailed explanation goes here
	import write.py
	
	OSCadd = "USB0::0x0957::0x9013::MY50270101::0::INSTR"
	Command = ":FREQ:RAST " + str(frequency)

	return = write(OSCadd,Command)