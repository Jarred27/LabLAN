function [errCode,errorDescription] = pingTest()
% checks python version and file/server avaliability
% Usage:
%	[errorCode,errorDescription]=pingTest();
% Inputs:
% 	none
% Outputs:
% 	errorCode:
% 		0 = no error
% 		1 = python not found
% 		11 = python wrong version
% 		2 = pingtest.py file not found, wrong directory???
% 		10060 = TCP error host not found
% 		3 = AWG comunication error, connont contact soft front panel?
%	errorDescription - string of error message from system call

[status,cmdOut] = system("python --version");
if status==1
    errCode=1;% python not installed
	errorDescription=cmdOut;
	return
end
if ~strcmp(cmdOut(1:8),'Python 3')
	if str2num(cmdOut(8))<3
		errCode=11; % python version error
		errorDescription="python version error";
		return
    end
end

[status,cmdOut] = system("python pingTest.py");
if status
	errCode = status;
	errorDescription=cmdOut;
	return
end

AWGadd = "AWG";
Command = "*IDN?";
cmdStr = "python query.py " + AWGadd + " " + Command;
[status,cmdOut] = system(cmdStr);
if status
	errCode = 3;
	errorDescription=cmdOut;
else
    errCode = 0;
	errorDescription=cmdOut;
end
end