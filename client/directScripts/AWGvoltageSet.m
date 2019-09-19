function AWGvoltageSet(channel,voltage)
% Applies the specified channel with the voltage given
% Usage:
%	AWGvoltageSet(channel,voltage);e.g.AWGvoltageSet(1,0.2)%0.2=200mV
% Inputs:
%	channel - int 1-4 of output channel to change
%	voltage - double of peak to peak voltage in Volts
% Outputs:
%	none

AWGadd = "TCPIP0::localhost::inst1::INSTR";
Command = "VOLT" + num2str(channel) + " " + num2str(voltage);

% in the form of ">python (python_command) (device) (device_command)"
cmdStr = "python write.py " + AWGadd + " " + Command;

[status,cmdOut] = system(cmdStr);
if status~=0
    warning("syetem error: "+cmdOut)
end
end