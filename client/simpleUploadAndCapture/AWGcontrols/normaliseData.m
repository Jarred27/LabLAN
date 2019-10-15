function normalisationFactor = normaiseData(fileName)
% overwrites the file at location of ../data_files within parent folder to within the range -1,1
% Usage:
%	normalisationFactor = normaiseData(fileName)
% Inputs:
%	fileName - string of file to be normalised
% Outputs:
%	normalisationFactor - value data is normalised by

cd ..
cd data_files

data=load(fileName);
normalisationFactor=max(abs(data))+0.0001;
data=data./normalisationFactor;
file=fopen(fileName,'wt');
for val=data'
	fprintf(file,'%1.8f\n',val);
end
fclose(file);

cd ..
cd AWGcontrols
end