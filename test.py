with open('test.txt', 'r') as myFile:
	data = myFile.readlines()

print data[0].split('\t')
