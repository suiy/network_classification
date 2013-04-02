#!/usr/bin/env python
flowf=open('flow.csv','r')
packet_avgf=open('flow_avg.csv','w+')
packet_maxf=open('flow_max.csv','w+')
packet_minf=open('flow_min.csv','w+')
packet_firstf=open('flow_first.csv','w+')


for line in flowf:
	temp=line.split(',')
	packet_avg=0.0
	packet_max=0.0
	packet_min=2000.0
	line_avg=""
	line_max=""
	line_min=""
	line_first=""
	##average
	for packet in temp[7:]:
		packet_avg+=float(packet)
	packet_avg=packet_avg/len(temp[7:])
	##
	##max
	for packet in temp[7:]:
		if float(packet)>packet_max:
			packet_max=float(packet)
	##min
	for packet in temp[7:]:
		if float(packet)<packet_min:
			packet_min=float(packet)

	for packet in temp[0:6]:
		line_avg+=packet+','
	line_max=line_avg
	line_min=line_avg
	line_first=line_avg
	line_avg+=str(packet_avg)+'\n'
	line_max+=str(packet_max)+'\n'
	line_min+=str(packet_min)+'\n'
	line_first+=str(temp[7])+'\n'
	packet_avgf.write(line_avg)
	packet_maxf.write(line_max)
	packet_minf.write(line_min)
	packet_firstf.write(line_first)
flowf.close()
packet_avgf.close()
packet_maxf.close()
packet_minf.close()
packet_firstf.close()
