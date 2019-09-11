import write
import query
import sys
AWGadd = "TCPIP0::localhost::inst1::INSTR"


def ask(channel):
	# AWGoutput.ask		- ask desired channel if ON or OFF
	Command = ":OUTP" + str(channel) + "?"
	return query.query(AWGadd,Command)


def set(channel, ONorOFF):
	# AWGoutput.set		- set desired channel to ON or OFF
	Command = ":OUTP" + str(channel) + " " + str(ONorOFF)
	return write.write(AWGadd,Command)

	
if __name__ == "__main__":
	if len(sys.argv) == 2:		# ask
		CHAN = sys.argv[1]
		result = ask(CHAN)
		print(result)
	elif len(sys.argv) == 3:	# set
		CHAN = sys.argv[1]
		ONorOFF = sys.argv[2]
		result = set(CHAN,ONorOFF)
		print(result)
	else:
		print("err expected 1 or 2 arguments, got "+str(len(sys.argv)-1)+".")
		sys.exit(1)
