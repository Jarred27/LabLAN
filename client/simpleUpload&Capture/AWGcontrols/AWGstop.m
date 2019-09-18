function AWGstop()
%AWGSTOP sets stop



AWGadd = "TCPIP0::localhost::inst1::INSTR";
Command = ":ABOR";

% in the form of ">python (python_command) (device) (device_command)"
cmdStr = "python write.py " + AWGadd + " " + Command;

[status,cmdOut] = system(cmdStr);
if status==2
    warning("file note found")
end