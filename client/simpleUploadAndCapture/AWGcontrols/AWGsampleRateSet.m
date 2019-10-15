function AWGsampleRateSet(frequency)
% sets AWG sample rate to the given frequency
% Usage:
%	AWGsampleRateSet(frequency); e.g. AWGsampleRateSet(8e8);%setting sample rate to 800 MHz
% Inputs:
%	frequency - sample rate frequency to be set
% Outputs:
%	none


AWGadd = "AWG";
Command = ":FREQ:RAST " + num2str(frequency);

% in the form of ">python (python_command) (device) (device_command)"
cmdStr = "python write.py " + AWGadd + " " + Command;

[status,cmdOut] = system(cmdStr);
if status~=0
    warning("syetem error: "+cmdOut)
end
end