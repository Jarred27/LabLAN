import write
import sys
AWGadd = "TCPIP0::localhost::inst1::INSTR"


def stop():
	# AWGstop.stop
	Command = ":ABOR"
	return write.write(AWGadd,Command)
	

if __name__ == "__main__":
	if len(sys.argv) == 1:		# stop
		result = stop()
		print(result)
	else:
		print("err expected 1 or 2 arguments, got "+str(len(sys.argv)-1)+".")
		sys.exit(1)