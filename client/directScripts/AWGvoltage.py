import write
import query
import sys
AWGadd = "TCPIP0::localhost::inst1::INSTR"


def ask(channel):
	# AWGvoltage.ask		- ask voltage of channel
	Command = "VOLT" + str(channel) + "?"
	return query.query(AWGadd,Command)


def set(channel, voltage):
	# AWGvoltage.set		- set voltage of channel
	Command = "VOLT" + str(channel) + " " + str(voltage)
	return write.write(AWGadd,Command)
	
	
if __name__ == "__main__":
	if len(sys.argv) == 2:		# ask
		CHAN = sys.argv[1]
		result = ask(CHAN)
		print(result)
	elif len(sys.argv) == 3:	# set
		CHAN = sys.argv[1]
		VOLT = sys.argv[2]
		result = set(CHAN,VOLT)
		print(result)
	else:
		print("err expected 1 or 2 arguments, got "+str(len(sys.argv)-1)+".")
		sys.exit(1)
