function voltage = AWGvoltageQuery(channel)
%AWGVOLTAGEQUERY Summary of this function goes here
%channel 


AWGadd = "TCPIP0::localhost::inst1::INSTR"
Command = "VOLT" + num2str(channel) + "?"

% in the form of ">python (python_command) (device) (device_command)"
cmdStr = "python query.py " + AWGadd + " " + Command;

[status,cmdOut] = system(cmdStr);
if status==2
    warning("file note found")
elseif status==0
	voltage = str2num(cmdOut)
end
return voltage
end