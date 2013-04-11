#!/usr/bin/env python
#this program extracts the flow statistics
flowf=open('flow_name.csv','r')
packet_avgf=open('flow_avg.csv','w+')
packet_maxf=open('flow_max.csv','w+')
packet_minf=open('flow_min.csv','w+')
packet_firstf=open('flow_first.csv','w+')
packet_twof=open('flow_two.csv','w+')
packet_threef=open('flow_three.csv','w+')
packet_fourf=open('flow_four.csv','w+')
packet_fivef=open('flow_five.csv','w+')
packet_avgf.write("sip,sport,dip,dport,time,app,protocol,statistics\n")
packet_maxf.write("sip,sport,dip,dport,time,app,protocol,statistics\n")
packet_minf.write("sip,sport,dip,dport,time,app,protocol,statistics\n")
packet_firstf.write("sip,sport,dip,dport,time,app,protocol,statistics\n")
packet_twof.write("sip,sport,dip,dport,time,app,protocol,p1,p2\n")
packet_threef.write("sip,sport,dip,dport,time,app,protocol,p1,p2,p3\n")
packet_fourf.write("sip,sport,dip,dport,time,app,protocol,p1,p2,p3,p4\n")
packet_fivef.write("sip,sport,dip,dport,time,app,protocol,p1,p2,p3,p4,p5\n")

flowf.readline()
for line in flowf:
	temp=line.split(',')
	packet_avg=0.0
	packet_max=0.0
	packet_min=2000.0
	line_avg=""
	line_max=""
	line_min=""
	line_first=""
	if len(temp)<13:
	#	print temp
		continue
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

	for packet in temp[0:7]:
		line_avg+=packet+','
	line_max=line_avg
	line_min=line_avg
	line_first=line_avg
	line_two=line_avg
	line_three=line_avg
	line_four=line_avg
	line_five=line_avg
	line_avg+=str(packet_avg)+'\n'
	line_max+=str(packet_max)+'\n'
	line_min+=str(packet_min)+'\n'
	line_first+=str(temp[7])+'\n'
	line_two+=str(temp[7])+','+str(temp[8])+'\n'
	line_three+=str(temp[7])+','+str(temp[8])+','+str(temp[9])+'\n'
	line_four+=str(temp[7])+','+str(temp[8])+','+str(temp[9])+','+str(temp[10])+'\n'
	line_five+=str(temp[7])+','+str(temp[8])+','+str(temp[9])+','+str(temp[10])+','+str(temp[11])+'\n'

	packet_avgf.write(line_avg)
	packet_maxf.write(line_max)
	packet_minf.write(line_min)
	packet_firstf.write(line_first)
	packet_twof.write(line_two)
	packet_threef.write(line_three)
	packet_fourf.write(line_four)
	packet_fivef.write(line_five)
flowf.close()
packet_avgf.close()
packet_maxf.close()
packet_minf.close()
packet_firstf.close()
packet_twof.close()
packet_threef.close()
packet_fourf.close()
packet_fivef.close()
