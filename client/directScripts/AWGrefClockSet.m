function AWGrefClockSet(frequency)
%AWGREFCLOCKSET Summary of this function goes here
%frequency - should be in Hz


AWGadd = "TCPIP0::localhost::inst1::INSTR"
Command = ":ROSC:FREQ " + num2str(frequency)

% in the form of ">python (python_command) (device) (device_command)"
cmdStr = "python write.py " + AWGadd + " " + Command;

[status,cmdOut] = system(cmdStr);
if status==2
    warning("file note found")
end