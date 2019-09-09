function OSCrun()
%OSCRUN Summary of this function goes here
OSCadd = "___"
Command = "___"

% in the form of ">python (python_command) (device) (device_command)"
cmdStr = "cd .. & " + "python write.py " + OSCadd + Command;

[status,cmdOut] = system(cmdStr);
if status==2
    warning("file note found")
end