function AWGrefClockSet(frequency)
% AWGrefClockSet(frequency) applies the frequency provided to the AWG external referenc clock setting
% Usage:
%	AWGrefClockSet(frequency); e.g. AWGrefClockSet(100e9);%set referenc clock 100 GHz
% Inputs:
%	frequency - Hz
% Outputs:
%	none


AWGadd = "AWG";
Command = ":ROSC:FREQ " + num2str(frequency);

% in the form of ">python (python_command) (device) (device_command)"
cmdStr = "python write.py " + AWGadd + " " + Command;

[status,cmdOut] = system(cmdStr);
if status~=0
    warning("syetem error: "+cmdOut)
end
end