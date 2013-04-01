#!/usr/bin/env python
import sys
truthf=open("1.csv",'r')
resultf=open("result.csv",'w+')
truthDic={}
for line in truthf:
	temp=line.split(',')
	index=[]
	data=[]
	index.append(temp[0])#sip
	index.append(temp[1])#sport
	index.append(temp[2])#dip
	index.append(temp[3])#dport
	data.append(temp[4])#time
	data.append(temp[5])#app
	data.append(temp[6])#protocol
	if len(temp)>7:
		for tmp in temp[7:]:
			data.append(tmp)#packet size list
	index_s=','.join(index)
	data_s=','.join(data)
	if truthDic.has_key(index_s):
		tmp=truthDic[index_s]
		truthDic[index_s]=tmp+';'+data_s[:-1]#for those flows with the same key, I put the values in a semicolon seperated string
		continue
	truthDic[index_s]=data_s[:-1]#put all the data of groundtruth in a dictionary
#print index_s
#print truthDic[index_s] 

def modify_value(time_s,truthdata,packet_size):
	ptime=float(time_s)
	multiple=truthdata.split(';')
	index=0
	minv=1001
	mini=0
	for truth in multiple:
		fields=truth.split(',')
		ttime=float(fields[0])
		if minv > abs(ttime-ptime):
			minv=abs(ttime-ptime)
			mini=index
		index+=1
	if minv >1000:
		return 0
	multiple[mini]=multiple[mini]+','+packet_size
	return ';'.join(multiple)
def check(str):#search for entry in groundtruth for the same sip,sport,dip and dport
	file=open(str,'r')
	file.readline()
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
			if modified_truth_value!=0:
				truthDic[index_s]=modified_truth_value

	file.close()

check("1002_5.csv")
for key,value in truthDic.items():
	if len(value.split(';'))==1:
		resultf.write(key+','+value+'\n')
		continue
	values=value.split(';')
	for val in values:
		resultf.write(key+','+val+'\n')
truthf.close()
resultf.close()








	
