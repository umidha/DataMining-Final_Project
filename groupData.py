#!/usr/bin/python

myFile1 = open('city1.txt', 'r')
data = myFile1.readlines()
data = [data[i].replace('\n', '') for i in range(0, len(data))]
data = [data[i].replace('-', ' ') for i in range(0, len(data))]

myFile = open('citystore.txt', 'r')
data1 = myFile.readlines()
data1 = [data1[i].replace('\n', '').split('\t') for i in range(0, len(data1))]

d = {}

for i in range(0, len(data1)):
	if data1[i][1] in d:
		d[data1[i][1]].append(data1[i][0])
	else:
		d[data1[i][1]] = [data1[i][0]]

for i in range(0, len(data)):
		print list(set(d[data[i]])),';', data[i] 

