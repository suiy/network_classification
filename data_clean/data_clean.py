#By Yuan Sui
#delete imcomplete data: no ip, no important imformation,incorrect ip address
#SIP, SPort, DestIP, DestPort,Time,  Application, Protocol, Packet size list(less than 1000sec)
#Nothing was printed out when I ran this program.

import csv
import string
import os


def read_write(file,fileout):
	filein = open(file,'r')
	filein.readline()
	row = list()
	for line in filein:
		row = line.split(',')
		if check_ip(row[0]) or check_ip(row[2]):		#check if ip is right
			print line
			continue
		if string.atoi(row[1])<0 or string.atoi(row[3])<0:	#check if port > 0
			print line
			continue
		if row[5]=="skype" or row[5]=="Skype.exe" or row[5]=="skypePM.exe" or row[5]=="Skype$$$$hdiutil$$$$bash$$$$cp":
			row[5]='Skype'
			s=''
			s='%s,%s,%s,%s,%s,%s,%s,%s' %(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
			fileout.write(s)
			continue
		if row[5]=="firefox-bin" or row[5]=="firefox.exe":
			row[5]='firefox'
			s=''
			s='%s,%s,%s,%s,%s,%s,%s,%s' %(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
			fileout.write(s)
			continue
		if row[5]=="thunderbird-bin" or row[5]=="thunderbird.exe":
			row[5]='thunderbird'
			s=''
			s='%s,%s,%s,%s,%s,%s,%s,%s' %(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
			fileout.write(s)
			continue
		if row[5]=="Safari Webpage P" or row[5]=="Safari Webpage":
			row[5]='Safari'
			s=''
			s='%s,%s,%s,%s,%s,%s,%s,%s' %(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
			fileout.write(s)
			continue
		if row[5]=="Transmission" or row[5]=="Mail" or row[5]=="bittorrent.exe" or row[5]=="amule" or row[5]=="ssh" or row[5]=="thunderbird" or row[5]=="svn":
			fileout.write(line)
			continue
		#if row[5]=="SVCHOST.EXE" or row[5]=="svchost.exe":
			#row[5]='svchost'
			#s=''
			#s='%s,%s,%s,%s,%s,%s,%s,%s' %(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
			#fileout.write(s)
			#continue 

		#fileout.write(line)
	fileout.close()
	filein.close()
def check_ip(ip):
	ip_list = list()
	ip_list = ip.split('.')
	for number in ip_list:
		if string.atoi(number)>255 or string.atoi(number)<0:
			return True
	return False

def re_print(file,fileout):
	fileout = open(fileout,'w')
	filein=open(file,'r')
	filein.readline()
	row = list()
	for line in filein:
		line=line.strip('\n')
		row = line.split(',')
		if (len(row)-7)<5:
			continue
		for index in range(7,len(row)): 
			s=''
			s='%s,%s,%s,%s,%s,%s,%s,%s\n' %(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[index])
			fileout.write(s)
	fileout.close()
	filein.close()

def print_app(file):
	filein = open(file,'r')
	filein.readline()
	row = list()
	app_list = list()
	for line in filein:
		row = line.split(',')
		if row[5] in app_list:
			continue
		else:
			app_list.append(row[5])
			print row[5]
	filein.close()

re_print('flow.csv','AfterClean1.csv')
#print_app('AfterClean1.csv')
fileout = open('AfterClean.csv','w')
fileout.write('Source_IP,Source_Port,Destination_IP,Destination_Port,Time,App,Protocol,Size\n')
read_write('AfterClean1.csv',fileout)
os.remove('AfterClean1.csv')
print_app('AfterClean.csv')