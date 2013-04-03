#!/usr/bin/env python
#this program simply removes the same records in groundtruth
filein=open('groundtruth.log','r')
fileout=open('groundtruth.csv','w+')
prev=""
for line in filein:
	if line!=prev:
		fileout.write(line)
	prev=line
filein.close()
fileout.close()
