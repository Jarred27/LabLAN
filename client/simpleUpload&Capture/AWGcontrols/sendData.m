function sendData(dataFileFolder,fileName,channelNumber)
% calls both transferFile.py and uploadFile.py files on a txt file in data_files folder

cmdStr = "python transferFile.py " + dataFileFolder + fileName + " " + fileName;
[status,cmdOut] = system(cmdStr);
if status
	error(cmdOut)
end

cmdStr = "python uploadFile.py " + fileName + " " + channelNumber;
[status,cmdOut] = system(cmdStr);
if status
	error(cmdOut)
end
end