function errString = AWGpollError()
%AWGREFCLOCKQUERY Summary of this function goes here



AWGadd = "TCPIP0::localhost::inst1::INSTR";
Command = ":SYST:ERR?";

% in the form of ">python (python_command) (device) (device_command)"
cmdStr = "python query.py " + AWGadd + " " + Command;

[status,cmdOut] = system(cmdStr);
if status==2
    warning("file not found")
elseif status==0
	errString = cmdOut;
end