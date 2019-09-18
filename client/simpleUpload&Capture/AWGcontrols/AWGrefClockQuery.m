function frequency = AWGrefClockQuery()
%AWGREFCLOCKQUERY Summary of this function goes here



AWGadd = "TCPIP0::localhost::inst1::INSTR";
Command = ":ROSC:FREQ?";

% in the form of ">python (python_command) (device) (device_command)"
cmdStr = "python query.py " + AWGadd + " " + Command;

[status,cmdOut] = system(cmdStr);
if status==2
    warning("file note found")
elseif status==0
	frequency = str2num(cmdOut);
end
end