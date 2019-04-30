function createTFW(inputSignal, filename)

%
%     createTFW(inputSignal, filename)
%
%
% INPUT:
%  inputSignal: must be between 1.0 and -1.0
%  filename: must have .tfw extension
%

%
% LAST MODIF. DATE: 24/05/2016 by Martin Sanz
% 



% header
fid = fopen(filename, 'w');
headerHex = ['54';'45';'4B';'41';'46';'47';'33';'30';'30';'30';'00';'00';'00';'00';'00';'00';'01';'31';'F0';'C2'];
header = hex2dec(headerHex);
fwrite(fid, header, 'uint8');

% signal length
lengthSignalHex = sprintf('%08X', length(inputSignal));
fwrite(fid, hex2dec(reshape(lengthSignalHex,[2 length(lengthSignalHex)/2])'), 'uint8');

% finishing header
fwrite(fid, uint8([0;0;0;1]), 'uint8');


% preview of signal
%fwrite(fid, uint8(ones(412,1)), 'uint8');
resampledSignal = resample(inputSignal,412,length(inputSignal));
resampledSignal(resampledSignal>1) = 1;
resampledSignal(resampledSignal<-1) = -1;
resampledSignal8b = uint8(round((resampledSignal+1)/2 * 255));
for p=1:2:length(resampledSignal8b)-1
    if resampledSignal8b(p)>resampledSignal8b(p+1)
        resampledSignal8b(p:p+1) = resampledSignal8b(p+1:-1:p);
    end
end
fwrite(fid, resampledSignal8b, 'uint8');

% zero block
fwrite(fid, uint8(zeros(72,1)), 'uint8');

% writing the signal
maxValue = 16382;
inputSignal(inputSignal>1) = 1;
inputSignal(inputSignal<-1) = -1;

inputSignal16b = uint16(round((inputSignal + 1)/2 * maxValue));
inputSignal16b = swapbytes(inputSignal16b);
fwrite(fid, inputSignal16b, 'uint16');



fclose(fid);

fprintf(['File ' filename ' written\n']);

end