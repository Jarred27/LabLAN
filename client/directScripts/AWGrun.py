import write
import query
import sys
AWGadd = "TCPIP0::localhost::inst1::INSTR"


def run():
	# AWGrun.run
	Command = ":INIT:IMM"
	return write.write(AWGadd,Command)

	
if __name__ == "__main__":
	if len(sys.argv) == 1:		# run
		result = run()
		print(result)
	else:
		print("err expected 1 or 2 arguments, got "+str(len(sys.argv)-1)+".")
		sys.exit(1)