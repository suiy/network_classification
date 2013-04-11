#!/usr/bin/env python
##this program extracts the flows from flow_five.csv of those two applications: firefox and safari
flow_10app=open('flow_five.csv','r')
flow_2app=open('flow_five_2app.csv','w')

flow_2app.write(flow_10app.readline())
firec=0
safac=0
for line in flow_10app:
	temp=line.split(',')
	if temp[5]=="firefox" :
		firec+=1
		flow_2app.write(line)
	if temp[5]=="Safari" :
		safac+=1
		flow_2app.write(line)

flow_10app.close()
flow_2app.close()

