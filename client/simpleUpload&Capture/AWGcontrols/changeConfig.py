import sys

# this file / function overwrites the config.txt file with a given config_<fileSuffix>.txt file

def changeConfig(fileSuffix):
	readFile = open('config_' + fileSuffix + '.txt', 'rb')
	writeFile = open("config.txt",'wb')
	line = readFile.read()
	while (line):
		writeFile.write(line)
		line = readFile.read()
	readFile.close()
	writeFile.close()
	

if __name__=="__main__":
	if len(sys.argv) == 2:
		fileSuffix=sys.argv[1]
		changeConfig(fileSuffix)
		sys.exit(0)
	else:
		print("expected 1 arguments got "+str(len(sys.argv)-1)+"\ncorrect usage: changeConfig file_suffix")
		sys.exit(1)