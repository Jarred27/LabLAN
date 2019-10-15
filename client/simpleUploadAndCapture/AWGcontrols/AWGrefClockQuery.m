function frequency = AWGrefClockQuery()
% AWGrefClockQuery() returns the external refrence clock setting of the AWG
% Usage:
%	frequency = AWGrefClockQuery();
% Inputs:
%	none
% Outputs:
%	frequency - Hz


AWGadd = "AWG";
Command = ":ROSC:FREQ?";

% in the form of ">python (python_command) (device) (device_command)"
cmdStr = "python query.py " + AWGadd + " " + Command;

[status,cmdOut] = system(cmdStr);
if status~=0
    warning("syetem error: "+cmdOut)
	frequency=nan;%not a number
end
frequency = str2num(cmdOut);
end