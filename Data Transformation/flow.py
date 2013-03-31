#!/usr/bin/env python
resultp=open("result.csv",'r')
flowp=open("flow.csv",'w+')
packetDic={}
app_diff=0
replication=0
for line in resultp:
	temp_line=line.split(',')
	index=[]
	data=[]
	index.append(temp_line[6])#protocol
	index.append(temp_line[1])#sip
	index.append(temp_line[2])#sport
	index.append(temp_line[3])#dip
	index.append(temp_line[4])#dport
	data.append(temp_line[5])#app
	data.append(temp_line[0])#time
	data.append('1')#packet number
	data.append(temp_line[7])#packet size
	index_s=','.join(index)
	data_s=','.join(data)
	if packetDic.has_key(index_s):#determine whether the flow already exists
		replication+=1
		temp_str=packetDic[index_s]
		dicstr=temp_str.split(',')
		if dicstr[0]!=data[0]:#if the flow has different app, skip
			app_diff+=1
			continue
		packet_size=dicstr[2]
		packet_size_int=int(packet_size)
		packet_size_int+=1#add the packet number by 1
		final=dicstr[0]+','+dicstr[1]+','+str(packet_size_int)+','+data[3][:-1]
		for packet in dicstr[3:]:#add the previous packet size back to the string
			final+=','+packet
		packetDic[index_s]=final#modify the packet dictionary
		continue
	packetDic[index_s]=data_s

print app_diff
print len(packetDic)
print replication

for key,value in packetDic.items():
	flowp.write(key+','+value)

resultp.close()
flowp.close()







	
