#!/usr/bin/python

myFile = open('cities.txt', 'r')
data = myFile.readlines()

print len(list(set(data)))
