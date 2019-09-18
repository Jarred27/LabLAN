function AWGvoltageSet(channel,voltage)
%AWGVOLTAGESET Summary of this function goes here
%channel
%voltage 

AWGadd = "TCPIP0::localhost::inst1::INSTR"
Command = "VOLT" + num2str(channel) + " " + num2str(voltage)

% in the form of ">python (python_command) (device) (device_command)"
cmdStr = "python write.py " + AWGadd + " " + Command;

[status,cmdOut] = system(cmdStr);
if status==2
    warning("file note found")
end