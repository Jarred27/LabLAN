import write
import query
import sys
OSCadd = "USB0::0x0957::0x9013::MY50270101::0::INSTR"


def ask():
	# OSCsampleRate.ask		- ask frequency of OSC
	Command = ":FREQ:RAST?"
	return query.query(OSCadd,Command)


def set(frequency):
	# OSCsampleRate.set		- set frequency of OSC
	Command = ":FREQ:RAST " + str(frequency)
	return write.write(OSCadd,Command)

	
if __name__ == "__main__":
	if len(sys.argv) == 1:		# ask
		result = ask()
		print(result)
	elif len(sys.argv) == 2:	# set
		FREQ = sys.argv[1]
		result = set(FREQ)
		print(result)
	else:
		print("err expected 1 or 2 arguments, got "+str(len(sys.argv)-1)+".")
		sys.exit(1)