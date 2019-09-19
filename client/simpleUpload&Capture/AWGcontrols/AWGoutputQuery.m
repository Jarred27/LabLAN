function outputState = AWGoutputQuery(channel)
% reads and returns the output state of the provided channel
% note that the AWGrun() function is required to begin generation on channels with output enabled
% Usage:
%	outputState=AWGoutputQuery(channel); e.g. channel_3_output_state=AWGoutputQyery(3);
% Inputs:
%	channel - int channel number of channel to read 
% Outputs:
%	outputState - returned enable state of channel


AWGadd = "TCPIP0::localhost::inst1::INSTR";
Command = ":OUTP" + num2str(channel) + "?";

% in the form of ">python (python_command) (device) (device_command)"
cmdStr = "python query.py " + AWGadd + " " + Command;

[status,cmdOut] = system(cmdStr);
if status~=0
    warning("syetem error: "+cmdOut)
	outputState=nan;%not a number
else
	outputState=num2str(cmdOut);
end
end