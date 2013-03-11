By Yuan Sui
#delete imcomplete data: no ip, no important imformation,incorrect ip address
import csv
import string


def read_write(file):
	filein = open(file,'r')
	filein.readline()
	row = list()
	for line in filein:
		row = line.split(',')
		if check_ip(row[1]) or check_ip(row[3]):
			print line
		if string.atoi(row[2])<0 or string.atoi(row[4])<0:
			print line

def check_ip(ip):
	ip_list = list()
	ip_list = ip.split('.')
	for number in ip_list:
		if string.atoi(number)>255 or string.atoi(number)<0:
			return True
	return False

read_write('log.csv')