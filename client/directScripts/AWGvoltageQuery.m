function voltage = AWGvoltageQuery(channel)
% Reads and returns the current peak to peak voltage setting on the specified channel number
% Usage:
%	voltage = AWGvoltageQuery(channel);e.g.channel_1_voltage = AWGvoltageSet(1);%(in Volts)
% Inputs:
%	channel - int 1-4 of output channel to read
% Outputs:
%	voltage - double of peak to peak voltage in Volts


AWGadd = "TCPIP0::localhost::inst1::INSTR";
Command = "VOLT" + num2str(channel) + "?";

% in the form of ">python (python_command) (device) (device_command)"
cmdStr = "python query.py " + AWGadd + " " + Command;

[status,cmdOut] = system(cmdStr);
if status!=0
    warning("syetem error: "+cmdOut)
	voltage=nan;%not a number response when error in system call
else
	voltage = str2num(cmdOut)
end
end