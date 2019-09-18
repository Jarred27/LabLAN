function normalisationFactor = normaiseData(fileName)
% redueces the value of all values in the given file at location of ../data_files within parent folder to within the range -1,1

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