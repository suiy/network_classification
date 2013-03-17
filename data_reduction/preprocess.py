# This program is to convert the "groundtruth.log" to the .csv file.

import csv
import string

def read_write(file,fileout):
  filein = open(file,'r')
  filein.readline()
  row = list()
  for line in filein:
    s = []
    row = line.split(':')
    s.append(row[0]+',')
    s.append(row[1]+',')
    s.append(row[3]+',')
    s.append(row[2]+',')
    s.append(row[4]+',')
    s.append(row[6]+',')
    s.append(row[7])
    fileout.write(''.join(s))
  filein.close()

fileout = open('log.csv','w')
fileout.write('Time,Source_IP,Source_Port,Destination_IP,Destination_Port,App,Protocol\n')
read_write('groundtruth.log',fileout)
fileout.close()
