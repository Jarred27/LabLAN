function sendData(dataFileFolder,fileName,channelNumber)
% calls both transferFile.py and uploadFile.py files on a txt file in data_files folder
% the function errors if the system call returns an error but does not test if AWG itself declined the data, use AWGpollError() to confirm data accepted
% Usage: 
%	sendData(dataFileFolder,fileName,ChannelNumber)
% Inputs:
%	dataFileFolder - e.g. "../data_files/" ,describes the location of the files relative to the python scripts being ran in the MATLAB current directory, can also pass full folder path
%	fileName - file including extention e.g. "tmp_real_X.txt"
%	channelNumber - channel number to upload file to
% Outputs:
% 	none

cmdStr = "python transferFile.py " + dataFileFolder + fileName + " " + fileName;
[status,cmdOut] = system(cmdStr);
if status
	error(cmdOut)
end

cmdStr = "python uploadFile.py " + fileName + " " + channelNumber + " AWG";
[status,cmdOut] = system(cmdStr);
if status
	error(cmdOut)
end
end