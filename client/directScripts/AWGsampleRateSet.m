function AWGsampleRateSet(frequency)
%AWGSAMPLERATESET Summary of this function goes here
%frequency 

AWGadd = "TCPIP0::localhost::inst1::INSTR "
Command = ":FREQ:RAST " + string(frequency)

% in the form of ">python (python_command) (device) (device_command)"
cmdStr = "cd .. & " + "python write.py " + AWGadd + Command;

[status,cmdOut] = system(cmdStr);
if status==2
    warning("file note found")
end