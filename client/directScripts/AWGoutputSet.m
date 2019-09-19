function AWGoutputSet(channel,ONorOFF)
% sets the output enable state of the given channel to the given state
% Usage:
%	AWGoutputSet(cnannel_number,ONorOFF);
% Inputs:
%	channel - int of channel number to set
%	ONorOFF - state to set, can be number 0 or 1 or string "off" or "on"
% Outputs:
%	none

AWGadd = "TCPIP0::localhost::inst1::INSTR";
Command = ":OUTP" + num2str(channel) + " " + num2str(ONorOFF);

% in the form of ">python (python_command) (device) (device_command)"
cmdStr = "python write.py " + AWGadd + " " + Command;

[status,cmdOut] = system(cmdStr);
if status!=0
    warning("syetem error: "+cmdOut)
end
end