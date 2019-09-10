function frequency = AWGsampleRateQuery()
%AWGsampleRateQuery Summary of this function goes here



AWGadd = "TCPIP0::localhost::inst1::INSTR"
Command = ":FREQ:RAST?"

% in the form of ">python (python_command) (device) (device_command)"
cmdStr = "cd .. & " + "python query.py " + AWGadd + " " + Command;

[status,cmdOut] = system(cmdStr);
if status==2
    warning("file note found")
elseif status==0
	frequency = str2num(cmdOut)
end
return frequency
end