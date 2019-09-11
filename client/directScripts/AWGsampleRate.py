import write
import query
import sys
AWGadd = "TCPIP0::localhost::inst1::INSTR"


def ask():
	# AWGsampleRate.ask		- ask frequency of DAC
	Command = ":FREQ:RAST?"
	return query.query(AWGadd,Command)


def set(frequency):
	# AWGsampleRate.set		- set frequency of DAC
	Command = ":FREQ:RAST " + str(frequency)
	return write.write(AWGadd,Command)

	
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