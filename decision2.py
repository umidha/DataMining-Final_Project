#!/usr/bin/python

from sklearn import tree
import numpy as np
import matplotlib.pyplot as plt


myFile = open('trainingData2.txt','r')
X = myFile.readlines()

for i in range(0, len(X)):
	X[i] = X[i].replace('\n','').split('\t')
	X[i] = [int(X[i][j]) for j in range(0, len(X[i]))]

myFile.close()

myFile = open('trainingClass2.txt', 'r')
Y = myFile.readlines()
for i in range(0, len(X)):
    Y[i] = int(Y[i].replace('\n',''))
    
myFile.close()

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

with open('graph2.dot','w') as f:
	f = tree.export_graphviz(clf, out_file=f)

myFile = open('testData2.txt', 'r')
testData = myFile.readlines()

for i in range(0, len(testData)):
	testData[i] = testData[i].replace('\n','').split('\t')
	testData[i] = [int(testData[i][j]) for j in range(0, len(testData[i]))]

result =  clf.predict(testData)
correct = 0
for i in range(0, len(result)):
	print result[i]
	if result[i] == Y[i]:
		correct += 1

print float(correct)/len(result)
