function voltage = AWGvoltageQuery(channel)
%AWGVOLTAGEQUERY Summary of this function goes here
AWGadd = "TCPIP0::localhost::inst1::INSTR "
Command = "___"

% in the form of ">python (python_command) (device) (device_command)"
cmdStr = "cd .. & " + "python write.py " + AWGadd + Command;

[status,cmdOut] = system(cmdStr);
if status==2
    warning("file note found")
end