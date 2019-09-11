import write
import query
import sys
AWGadd = "TCPIP0::localhost::inst1::INSTR"


def err():
	# AWGrun.run
	Command = ":SYST:ERR?"
	return query.query(AWGadd,Command)

	
if __name__ == "__main__":
	if len(sys.argv) == 1:		# run
		result = err()
		print(result)
	else:
		print("err expected 0 arguments, got "+str(len(sys.argv)-1)+".")
		sys.exit(1)