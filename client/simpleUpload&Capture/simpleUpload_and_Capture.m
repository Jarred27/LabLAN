%%%simple scope capture
clear all;
close all;
clc;

delete(instrfind)

addpath('lean scope interface')

AWGvoltagePeaktoPeak=0.2; % V
files=["tmp_real_X.txt","tmp_imag_X.txt","tmp_real_y.txt","tmp_imag_y.txt"]; % files in /data_files/

%% send AWG data
cd AWGcontrols % entering folder where python scripts call from
[AWG_link_status,AWG_link_error]=pingTest();
if AWG_link_status
	cd ..
	error("error in contacting AWG, errCode: "+AWG_link_status+AWG_link_error)
end
% clear error log
while(1)
	errStr=AWGpollError();
	if errStr(1)=='0'
		break
	end
end

AWGstop()

% check if files require normalising
for fileName=files
	normalisationFactor=normaliseData(fileName);
	if normalisationFactor~=1
		warning("normalising "+fileName+" by "+num2str(normalisationFactor)) % this is normal so consider supressing
	end
end

% upload X_real to channel 1
sendData('../data_files/',files(1),1);
pause(1) %waiting for AWG to interpret waveform before checking errors
% check error log
errStr=AWGpollError();
if errStr(1)~='0'
	warning(errStr)
end

% upload X_imaj to channel 2
sendData('../data_files/',files(2),2);
pause(1) %waiting for AWG to interpret waveform before checking errors
% check error log
errStr=AWGpollError();
if errStr(1)~='0'
	warning(errStr)
end

% upload Y_real to channel 3
sendData('../data_files/',files(3),3);
pause(1) %waiting for AWG to interpret waveform before checking errors
% check error log
errStr=AWGpollError();
if errStr(1)~='0'
	warning(errStr)
end

% upload Y_imaj to channel 4
sendData('../data_files/',files(4),4);
pause(1) %waiting for AWG to interpret waveform before checking errors
% check error log
errStr=AWGpollError();
if errStr(1)~='0'
	warning(errStr)
end

%enable and run all channels
AWGoutputSet(1,1);
AWGoutputSet(2,1);
AWGoutputSet(3,1);
AWGoutputSet(4,1);
AWGvoltageSet(1,AWGvoltagePeaktoPeak);
AWGvoltageSet(2,AWGvoltagePeaktoPeak);
AWGvoltageSet(3,AWGvoltagePeaktoPeak);
AWGvoltageSet(4,AWGvoltagePeaktoPeak);
%AWGrun();

cd .. % returning to parent folder

%% get data from scope

scope_obj = initiliseScopeLean('follower','switch','agilent');
[k,XI,XQ,YI,YQ] = getDataLean(scope_obj);
