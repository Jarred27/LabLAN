function AWGrun()
% starts signal generation on enabled outputs
% Usage:
%	AWGrun();
% Inputs:
%	none
% Outputs:
%	none


AWGadd = "AWG";
Command = ":INIT:IMM";

% in the form of ">python (python_command) (device) (device_command)"
cmdStr = "python write.py " + AWGadd + " " + Command;

[status,cmdOut] = system(cmdStr);
if status~=0
    warning("syetem error: "+cmdOut)
end
end