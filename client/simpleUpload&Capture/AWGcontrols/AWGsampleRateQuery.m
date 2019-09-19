function frequency = AWGsampleRateQuery()
% reads and returns the current sample rate setting on the AWG
% Usage:
%	AWGsampleRateQuery();
% Inputs:
%	none
% Outputs:
%	frequency - current sample rate setting (Hz)



AWGadd = "TCPIP0::localhost::inst1::INSTR";
Command = ":FREQ:RAST?";

% in the form of ">python (python_command) (device) (device_command)"
cmdStr = "python query.py " + AWGadd + " " + Command;

[status,cmdOut] = system(cmdStr);
if status~=0
    warning("syetem error: "+cmdOut)
	frequency=nan;%not a number
else
	frequency = str2num(cmdOut);
end
end