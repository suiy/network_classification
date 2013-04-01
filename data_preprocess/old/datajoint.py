# This program is to create the .csv file about getting the packet size of each packet in "log.csv" from .pcap file and make the data joint.
# Ignore the print, they are just for check whether the program is right. We just the need the output file.
# I checked the "groundtruth.log" and found that there are about 6 duplicate logs. And about 4 logs which cannot find in .pcap files.

import csv

reader = csv.reader(open("log.csv"))
checkpacketList = []
logList = []
logDict = {}
for Time,Source_IP,Source_Port,Destination_IP,Destination_Port,App,Protocol in reader:
  unitList = []
  unitList_1 = []
  unitList.append(Time)
  unitList.append(Source_Port)
  unitList.append(Destination_IP)
  unitList.append(Destination_Port)
  unitList_1.append(Time)
  unitList_1.append(Source_IP)
  unitList_1.append(Source_Port)
  unitList_1.append(Destination_IP)
  unitList_1.append(Destination_Port)
  unitList_1.append(App)
  unitList_1.append(Protocol)
  unitStr = ','.join(unitList)
  unitStr_1 = ','.join(unitList_1)
  checkpacketList.append(unitStr)
  logList.append(unitStr_1)
checkpacketList.remove(checkpacketList[0])
logList.remove(logList[0])
for i in range(len(logList)):
  logDict[checkpacketList[i]] = logList[i]
checkpacketSet = set(checkpacketList)
print checkpacketList[1]
print logDict[checkpacketList[1]]

def addSize(file):
  filein = csv.reader(open(file,'r'))
  lengthList = []
  resultList = []
  for Time,Destination,Length,DPort,SrcAddr,SrcPort in filein:
    packetList = []
    packetList.append(Time)
    packetList.append(SrcPort)
    packetList.append(Destination)
    packetList.append(DPort)
    packetStr = ','.join(packetList)
    if logDict.has_key(packetStr):
      if checkValueChanged(logDict[packetStr]):
        logDict[packetStr] = logDict[packetStr]+','+Length+'\n'
      lengthList.append(logDict[packetStr])
  return lengthList

def checkValueChanged(str):
  n = 0
  for i in str:
    if i == ',':
      n = n+1
  if n == 7:
    return False
  else:
    return True

lengthList_0930 = addSize('0930.csv')
print len(lengthList_0930)
lengthList_1001 = addSize('1001.csv')
print len(lengthList_1001)
lengthList_10021 = addSize('1002_1.csv')
print len(lengthList_10021)
lengthList_10022 = addSize('1002_2.csv')
print len(lengthList_10022)
lengthList_10023 = addSize('1002_3.csv')
print len(lengthList_10023)
lengthList_10024 = addSize('1002_4.csv')
print len(lengthList_10024)
lengthList_10025 = addSize('1002_5.csv')
print len(lengthList_10025)
alllengthList = lengthList_0930 + lengthList_1001 + lengthList_10021 + lengthList_10022 + lengthList_10023 + lengthList_10024 + lengthList_10025
print len(alllengthList)
print len(set(alllengthList))
print alllengthList[0]
print alllengthList[1]

fileout = open('result.csv','w')
fileout.write('Time,Source_IP,Source_Port,Destination_IP,Destination_Port,App,Protocol,Size\n')
for each in alllengthList:
  fileout.write(each)
fileout.close()
