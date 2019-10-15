function errString = AWGpollError()
% querys the error buffer on the AWG, when the AWG recieves a bad command the function that sent it may not show the error but the AWG log will record it
% should be called after send data function to verify that it was uploaded without error
% if multiple errors are present in the AWG this needs to be called once for each, the error log is clear when errString(1)=='0'
% Usage:
%	errorString = AWGpollError();
% Inputs:
%	none
% Outputs:
%	errorString - string containing the top value of the AWG error buffer



AWGadd = "AWG";
Command = ":SYST:ERR?";

% in the form of ">python (python_command) (device) (device_command)"
cmdStr = "python query.py " + AWGadd + " " + Command;

[status,cmdOut] = system(cmdStr);
if status~=0
    warning("syetem error: "+cmdOut)
	errString="";
else
	errString = cmdOut;
end
end