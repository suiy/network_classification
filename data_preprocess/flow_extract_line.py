#!/usr/bin/env python
#this program combines pcap files and groundtruth to produce the final flow records.
import sys
truthf=open("groundtruth.csv",'r')
resultf=open("flow.csv",'w+')
truthDic={}
##remove the first line of groundtruth
truthf.readline()
for line in truthf:
	temp=line.split(':')
	index=[]
	data=[]
	index.append(temp[1])#sip
	index.append(temp[3])#sport
	index.append(temp[2])#dip
	index.append(temp[4])#dport
	data.append(temp[0])#time
	data.append(temp[6])#app
	data.append(temp[7][:-1])#protocol
	index_s=','.join(index)
	if truthDic.has_key(index_s):
		tmp=truthDic[index_s]
		tmp.append(data)
		truthDic[index_s]=tmp#for those flows with the same key, I put the values in a semicolon separated string
		continue
	truthDic[index_s]=[data]#put all the data of groundtruth in a dictionary
#print index_s #for test whether the dictionary is correctly constructed
#print truthDic[index_s] 

def modify_value(time_s,truthdata,packet_size):#param: time, groundtruth data, current packet size
	ptime=float(time_s)
	index=0
	minv=1000000
	mini=0
	for truth in truthdata:
		ttime=float(truth[0])
		if minv > abs(ttime-ptime) and ptime>=ttime:
			minv=abs(ttime-ptime)
			mini=index
		index+=1
	if minv ==1000000:
		return 0
	#temp=multiple[mini].split(',')
	#temp.append(packet_size)
	#multiple[mini]=','.join(temp)# this is the most time consuming part
	truthdata[mini].append(packet_size)
	return truthdata
def check(filein):#search for entry in groundtruth for the same sip,sport,dip and dport
	file=open(filein,'r')
	file.readline()#remove the first line of header
	packet_noflow=0
	count=1
	for line in file:
		sys.stdout.write('\r%d'%count)
		count+=1
		temp=line.split(',')
		index=[]
		index.append(temp[4][1:-1])#sip
		index.append(temp[5][1:-3])#sport
		index.append(temp[1][1:-1])#dip
		index.append(temp[3][1:-1])#dport
		index_s=','.join(index)
		data_s=temp[2][1:-1]
		if truthDic.has_key(index_s):
			truthdata=truthDic[index_s]
			modified_truth_value=modify_value(temp[0][1:-1],truthdata,data_s)
			if modified_truth_value!=0:#return 0 if there is no flows that it belongs to
				truthDic[index_s]=modified_truth_value
			else:
				packet_noflow+=1
	print "\nthe number of packets which belong to no flows is "+ str(packet_noflow)
	file.close()

check("allpcap.csv")
for key,value in truthDic.items():
	for flow in value:
		tmp=""
		for element in flow:
			tmp+=element+','
		tmp=tmp[:-1]
		resultf.write(key+','+tmp+'\n')
truthf.close()
resultf.close()








	
