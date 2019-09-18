function AWGoutputSet(channel,ONorOFF)
%AWGOUTPUTSET Summary of this function goes here
%channel is which channel you want 
%ONorOFF is either 1 or 0

AWGadd = "TCPIP0::localhost::inst1::INSTR";
Command = ":OUTP" + num2str(channel) + " " + num2str(ONorOFF);

% in the form of ">python (python_command) (device) (device_command)"
cmdStr = "python write.py " + AWGadd + " " + Command;

[status,cmdOut] = system(cmdStr);
if status==2
    warning("file note found")
end