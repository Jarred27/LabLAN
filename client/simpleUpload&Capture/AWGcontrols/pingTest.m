function errCode = pingTest()
% checks python version and file/server avaliability
% error codes:
% 0 = no error
% 1 = python not found
% 11 = python wrong version
% 2 = pingtest.py file not found, wrong directory???
% 10060 = TCP error host not found
% 3 = AWG comunication error, connont contact soft front panel?

[status,cmdOut] = system("python --version");
if status==1
    errCode=1;% python not installed
	return
end
if ~strcmp(cmdOut(1:8),'Python 3')
	if str2num(cmdOut(8))<3
		errCode=11; % python version error
		return
    end
end

[status,~] = system("python pingTest.py");
if status
	errCode = status;
	return
end

AWGadd = "TCPIP0::localhost::inst1::INSTR";
Command = "*IDN?";
cmdStr = "python query.py " + AWGadd + " " + Command;
[status,~] = system(cmdStr);
if status
	errCode = 3;
else
    errCode = 0;
end
end