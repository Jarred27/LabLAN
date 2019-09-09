function OSCrun()
%OSCRUN Summary of this function goes here
OSCadd = "USB0::0x0957::0x9013::MY50270101::0::INSTR "
Command = ":INIT:IMM"

% in the form of ">python (python_command) (device) (device_command)"
cmdStr = "cd .. & " + "python write.py " + OSCadd + Command;

[status,cmdOut] = system(cmdStr);
if status==2
    warning("file note found")
end