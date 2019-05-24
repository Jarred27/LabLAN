%%%%%%Generation of RRC filtered signals%%%%%
clear all; close all; clc
%addpath modules

L_target = 2^18; %%%total number of samples
Baud = 22; %%desired total baud rate [Gbd]
Nsc = 1; %%number of subcarriers
sep_fact=1.1; %% separation factor beyone sc rate ...
L_total = L_target;
DACrate = 64; %AWG sampling rate [GSa/s]
Att_stop = 35; %%%%Stop band attenuation
Beta = 0.025; %%%%%%Roll-off factor
dc_fact=0;
M = 64; %%%%%%% moindex-QAM (4 = 4-QAM = QPSK ...)


sps = 2;%floor(DACrate/(Baud/Nsc));
os = DACrate/(Baud/Nsc);

PE_on=0;

%%%%%%RRC filter design%%%%%
rrc = fdesign.pulseshaping(sps,'Square Root Raised Cosine','Ast,Beta',Att_stop,Beta);
rrc_filter = design(rrc);

L_header = 1000; %%%%%%some zeros
header_zero = zeros(L_header,1);

L_syn = 400;  %%%sync bits
temp = randi([0 1],L_syn,1);
synch = qammod(temp,2)*exp(1i*pi/4)*sqrt(M-(sqrt(M)/2+0.5)^2);

L_data = round((L_total-L_header*os-L_syn*os)/os)-1;
for ii_Nsc=1:Nsc
TxX_bits(ii_Nsc,:) = randi([0 M-1],L_data,1);
dataX(ii_Nsc,:) = qammod(TxX_bits(ii_Nsc,:),M,'gray');
TX(ii_Nsc,:) = [header_zero.' synch.' dataX(ii_Nsc,:)];
TxY_bits(ii_Nsc,:) = randi([0 M-1],L_data,1);
dataY(ii_Nsc,:) = qammod(TxY_bits(ii_Nsc,:),M,'gray');
TY(ii_Nsc,:) = [header_zero.' synch.' dataY(ii_Nsc,:)];
end

% figure(10)
% plot(real(dataX))
% axis([1 20 -6 6])
% figure(11)
% plot(20*log10(abs(fftshift(fft(dataX)))))


%%% pulse shape
up_x = upsample(TX.',sps);
RRC_x = filter(rrc_filter,up_x);
up_y = upsample(TY.',sps);
RRC_y = filter(rrc_filter,up_y);

% figure(20)
% plot(real(up_x))
% axis([1400*2 1400*2+40 -6 6])
% figure(21)
% plot(20*log10(abs(fftshift(fft(up_x)))))

% figure(30)
% plot(real(RRC_x))
% axis([1400*2 1400*2+40 -6 6])
% figure(31)
% plot(20*log10(abs(fftshift(fft(RRC_x)))))

up_x=resample(RRC_x,DACrate*1000,sps*Baud/Nsc*1000,100);
up_y=resample(RRC_y,DACrate*1000,sps*Baud/Nsc*1000,100);

TxX=[up_x;zeros(L_target-length(up_x(:,1)),Nsc)];
TxY=[up_y;zeros(L_target-length(up_y(:,1)),Nsc)];

% figure(40)
% plot(real(TxX))
% axis([1400*2 1400*2+40 -6 6])
% figure(41)
% plot(20*log10(abs(fftshift(fft(TxX)))))

t=(0:1:(length(TxX(:,1))-1))'/(DACrate*1e9); %time array for resampled data
f=linspace(-DACrate/2,DACrate/2,length(TxX(:,1))); %freq array for resampled data FFT

df=Baud/Nsc;
dfs=((0:1:(Nsc-1))*df-((Nsc-1)*df/2))*sep_fact;
TxX=(TxX+(dc_fact*log2(M))).*exp(-1i*2*pi*dfs*1e9.*t); %frequency shifted signal
TxY=(TxY+(dc_fact*log2(M))).*exp(-1i*2*pi*dfs*1e9.*t); %frequency shifted signal
TxX=sum(TxX,2);
TxY=sum(TxY,2);
 
figure(1); plot(t,real(TxX),'b'); hold on; plot(t,imag(TxX),'r');
figure(2); plot(f,20*log10(fftshift(abs(fft(TxX)))));

if PE_on==1;
    %apply optically measured preemphasis
    f_dsp=linspace(0,DACrate/2,length(TxX)/2)*1e-3; %sample domain frequnecy [THz]
    load('Sumi_64GSaps_50Gbd_PE_filt.mat');
    pe_filt_interp=interp1(f_ssb,pe_filt,f_dsp).';
    pe_filt_interp(isnan(pe_filt_interp))=max(pe_filt_interp(~isnan(pe_filt_interp)));
    pe_filt_dsp=[flipud(pe_filt_interp);pe_filt_interp];
    TxX_PE=ifft(ifftshift(fftshift(fft(TxX)).*sqrt(10.^(pe_filt_dsp/10))));
    TxY_PE=ifft(ifftshift(fftshift(fft(TxY)).*sqrt(10.^(pe_filt_dsp/10))));
    xreal_PE=real(TxX_PE);
    ximag_PE=imag(TxX_PE);
    yreal_PE=real(TxY_PE);
    yimag_PE=imag(TxY_PE);
    figure; plot(linspace(-DACrate/2,DACrate/2,length(TxX_PE)),20*log10(fftshift(abs(fft(TxX_PE)))))
end

if M==4
    form='QPSK';
else
    form=[num2str(M) 'QAM'];
end

sw=0;
while sw==0
    svar=input('Save data files? (y/n): ','s');
    if strcmp(svar,'y')==1
        sav_dir='data_files';
        if exist(sav_dir,'dir')~=7
            mkdir(sav_dir)
        end
        
        if PE_on==0
            fid = fopen([sav_dir '/' 'RRC_PM' form '_' num2str(Baud) 'Gbd_' num2str(Nsc) '_sc_' num2str(DACrate) 'Gsaps_real_X.txt'], 'wt');
            fprintf(fid, '%2.8f\n',real(TxX));
            fclose(fid);
            fid = fopen([sav_dir '/' 'RRC_PM' form '_' num2str(Baud) 'Gbd_' num2str(Nsc) '_sc_' num2str(DACrate) 'Gsaps_imag_X.txt'], 'wt');
            fprintf(fid, '%2.8f\n',imag(TxX));
            fclose(fid);
            fid = fopen([sav_dir '/' 'RRC_PM' form '_' num2str(Baud) 'Gbd_' num2str(Nsc) '_sc_' num2str(DACrate) 'Gsaps_' 'real_y.txt'], 'wt');
            fprintf(fid, '%2.8f\n',real(TxY));
            fclose(fid);
            fid = fopen([sav_dir '/' 'RRC_PM' form '_' num2str(Baud) 'Gbd_' num2str(Nsc) '_sc_' num2str(DACrate) 'Gsaps_' 'imag_y.txt'], 'wt');
            fprintf(fid, '%2.8f\n',imag(TxY));
            fclose(fid);
            namefile = [sav_dir '/' 'RRC_PM' form '_' num2str(Baud) 'Gbd_' num2str(Nsc) '_sc_' num2str(DACrate) 'Gsaps__transmit_data.mat'];
            save(namefile,'TxX','TxY','dataX','dataY','synch','rrc_filter','TxX_bits','TxY_bits');
            sw=1;
            
        elseif PE_on==1
            
            fid = fopen([sav_dir '/' 'RRC_PM' form '_' num2str(Baud) 'Gbd_' num2str(Nsc) '_sc_' num2str(DACrate) 'Gsaps_' 'real_x_PE.txt'], 'wt');
            fprintf(fid, '%2.8f\n',xreal_PE);
            fclose(fid);
            fid = fopen([sav_dir '/' 'RRC_PM' form '_' num2str(Baud) 'Gbd_' num2str(Nsc) '_sc_' num2str(DACrate) 'Gsaps_' 'imag_x_PE.txt'], 'wt');
            fprintf(fid, '%2.8f\n',ximag_PE);
            fclose(fid);
            fid = fopen([sav_dir '/' 'RRC_PM' form '_' num2str(Baud) 'Gbd_' num2str(Nsc) '_sc_' num2str(DACrate) 'Gsaps_' 'real_y_PE.txt'], 'wt');
            fprintf(fid, '%2.8f\n',yreal_PE);
            fclose(fid);
            fid = fopen([sav_dir '/' 'RRC_PM' form '_' num2str(Baud) 'Gbd_' num2str(Nsc) '_sc_' num2str(DACrate) 'Gsaps_' 'imag_y_PE.txt'], 'wt');
            fprintf(fid, '%2.8f\n',yimag_PE);
            fclose(fid);
            namefile = [sav_dir '/' 'RRC_PM' form '_' num2str(Baud) 'Gbd_' num2str(Nsc) '_sc_' num2str(DACrate) 'Gsaps_' '_transmit_data_PE.mat'];
            save(namefile,'TxX_PE','TxY_PE','dataX','dataY','synch','rrc_filter','TxX_bits','TxY_bits');
            sw=1;
            
        else
            display('PE switch badly defined, not saving')
            sw=1;
        end
    elseif strcmp(svar,'n')==1
        display('files not saved')
        sw=1;
    else
        sw=0;
    end
end