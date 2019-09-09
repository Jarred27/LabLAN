function AWGvoltageSet(channel,voltage)
%AWGVOLTAGESET Summary of this function goes here
%channel
%voltage 

AWGadd = "TCPIP0::localhost::inst1::INSTR "
Command = "VOLT" + string(channel) + " " + string(voltage)

% in the form of ">python (python_command) (device) (device_command)"
cmdStr = "cd .. & " + "python write.py " + AWGadd + Command;

[status,cmdOut] = system(cmdStr);
if status==2
    warning("file note found")
end