#flows=read.table("/Users/GaoNing/Desktop/DM Data/Flow/flow_min/AfterClean.csv",header=TRUE,sep=",",dec=".")
flows=read.table("/home/neal/Dropbox/DMSharing/Dataset/flow_min/AfterClean.csv",header=TRUE,sep=",",dec=".")
size=flows$Size##size of flows
app=flows$App##app of flows

plot(density(size))##plot the size density of all the flows
hist(size)

plot(flows,app,labels=row.names(app),xlab="Packet Size")##takes time
axis(2,at=app,labels=row.names(app))##not executed

skype=flows[flows$App=="Skype",]##application seperation
firefox=flows[flows$App=="firefox",]
transm=flows[flows$App=="Transmission",]
mail=flows[flows$App=="Mail",]
bittor=flows[flows$App=="bittorrent.exe",]
safari=flows[flows$App=="Safari",]
amule=flows[flows$App=="amule",]
ssh=flows[flows$App=="ssh",]
thunder=flows[flows$App=="thunderbird",]
svn=flows[flows$App=="svn",]
boxplot(skype$Size,firefox$Size,transm$Size,mail$Size,bittor$Size,safari$Size,amule$Size,ssh$Size,thunder$Size,svn$Size,names=c("skype","firefox","transmission","mail","bittorrent","safari","amule","ssh","thunderbird","svn"))#takes time
slices<-c(nrow(skype),nrow(firefox),nrow(transm),nrow(mail),nrow(bittor),nrow(safari),nrow(amule),nrow(ssh),nrow(thunder),nrow(svn))#not executed
pie(slices, label = c("skype","firefox","transmission","mail","bittorrent","safari","amule","ssh","thunderbird","svn"), main="Pie Chart of Apps")
hist(slices, label = c("skype","firefox","transmission","mail","bittorrent","safari","amule","ssh","thunderbird","svn"), main="Histgram Chart of Apps")
barplot(slices, names.arg = c("skype","firefox","transmission","mail","bittorrent","safari","amule","ssh","thunderbird","svn"), main="Bar Chart of Apps")

##histgram of each application
par(mfrow=c(2,5))
hist(skype$Size,main="Histogram of skype")
hist(firefox$Size,main="Histogram of firefox")
hist(transm$Size,main="Histogram of transmission")
hist(mail$Size,main="Histogram of mail")
hist(bittor$Size,main="Histogram of bittorrent")
hist(safari$Size,main="Histogram of safari")
hist(amule$Size,main="Histogram of amule")
hist(ssh$Size,main="Histogram of ssh")
hist(thunder$Size,main="Histogram of thunderbird")
hist(svn$Size,main="Histogram of svn")

##boxplot of each application TCP/UDP
boxplot(skype[skype$Protocol=="TCP",]$Size,skype[skype$Protocol=="UDP",]$Size,firefox[firefox$Protocol=="TCP",]$Size,firefox[firefox$Protocol=="UDP",]$Size,transm[transm$Protocol=="TCP",]$Size,transm[transm$Protocol=="UDP",]$Size,names=c("skype tcp","skype udp","firefox tcp","firefox udp","transmission tcp","transmission udp"))
boxplot(mail[mail$Protocol=="TCP",]$Size,mail[mail$Protocol=="UDP",]$Size,bittor[bittor$Protocol=="TCP",]$Size,bittor[bittor$Protocol=="UDP",]$Size,safari[safari$Protocol=="TCP",]$Size,safari[safari$Protocol=="UDP",]$Size,names=c("mail tcp","mail udp","bittorrent tcp","bittorrent udp","safari tcp","safari udp"))
boxplot(amule[amule$Protocol=="TCP",]$Size,amule[amule$Protocol=="UDP",]$Size,names=c("amule tcp","amule udp"))##error
boxplot(ssh[ssh$Protocol=="TCP",]$Size, ssh[ssh$Protocol=="UDP",]$Size,thunder[thunder$Protocol=="TCP",]$Size, thunder[thunder$Protocol=="UDP",]$Size,svn[svn$Protocol=="TCP",]$Size, svn[svn $Protocol=="UDP",]$Size,names=c("ssh tcp","ssh udp","thunderbird tcp","thunderbird udp","svn tcp","svn udp"))

##Skype plot
par(mfrow=c(2,2))
plot(skype$Time,skype$Size,xlab="Time",ylab="Size",main="Scatterplot of Time vs. Size")
plot(density(skype$Size),xlab="Size",main="Densityplot of Size")
hist(skype$Size,xlab="Size",main="Histogram of Size")
boxplot(skype$Size,ylab="Size",main="Boxplot of Size")

##firefox
par(mfrow=c(2,2))
plot(firefox$Time,firefox$Size,xlab="Time",ylab="Size",main="Scatterplot of Time vs. Size")
plot(density(firefox$Size),xlab="Size",main="Densityplot of Size")
hist(firefox$Size,xlab="Size",main="Histogram of Size")
boxplot(firefox$Size,ylab="Size",main="Boxplot of Size")

##transmission
par(mfrow=c(2,2))
plot(transm$Time, transm$Size,xlab="Time",ylab="Size",main="Scatterplot of Time vs. Size")
plot(density(transm$Size),xlab="Size",main="Densityplot of Size")
hist(transm$Size,xlab="Size",main="Histogram of Size")
boxplot(transm$Size,ylab="Size",main="Boxplot of Size")

##mail
par(mfrow=c(2,2))
plot(mail$Time, mail$Size,xlab="Time",ylab="Size",main="Scatterplot of Time vs. Size")
plot(density(mail$Size),xlab="Size",main="Densityplot of Size")
hist(mail $Size,xlab="Size",main="Histogram of Size")
boxplot(mail$Size,ylab="Size",main="Boxplot of Size")

##bittorrent
par(mfrow=c(2,2))
plot(bittor$Time, bittor$Size,xlab="Time",ylab="Size",main="Scatterplot of Time vs. Size")
plot(density(bittor$Size),xlab="Size",main="Densityplot of Size")
hist(bittor$Size,xlab="Size",main="Histogram of Size")
boxplot(bittor$Size,ylab="Size",main="Boxplot of Size")

##safari
par(mfrow=c(2,2))
plot(safari$Time, safari $Size,xlab="Time",ylab="Size",main="Scatterplot of Time vs. Size")
plot(density(safari$Size),xlab="Size",main="Densityplot of Size")
hist(safari $Size,xlab="Size",main="Histogram of Size")
boxplot(safari $Size,ylab="Size",main="Boxplot of Size")

##amule
par(mfrow=c(2,2))
plot(amule$Time, amule $Size,xlab="Time",ylab="Size",main="Scatterplot of Time vs. Size")
plot(density(amule$Size),xlab="Size",main="Densityplot of Size")
hist(amule $Size,xlab="Size",main="Histogram of Size")
boxplot(amule $Size,ylab="Size",main="Boxplot of Size")

##ssh
par(mfrow=c(2,2))
plot(ssh$Time, ssh $Size,xlab="Time",ylab="Size",main="Scatterplot of Time vs. Size")
plot(density(ssh$Size),xlab="Size",main="Densityplot of Size")
hist(ssh $Size,xlab="Size",main="Histogram of Size")
boxplot(ssh $Size,ylab="Size",main="Boxplot of Size")

##thunderbird
par(mfrow=c(2,2))
plot(thunder$Time, thunder$Size,xlab="Time",ylab="Size",main="Scatterplot of Time vs. Size")
plot(density(thunder$Size),xlab="Size",main="Densityplot of Size")
hist(thunder$Size,xlab="Size",main="Histogram of Size")
boxplot(thunder$Size,ylab="Size",main="Boxplot of Size")

##svn
par(mfrow=c(2,2))
plot(svn$Time, svn $Size,xlab="Time",ylab="Size",main="Scatterplot of Time vs. Size")
plot(density(svn $Size),xlab="Size",main="Densityplot of Size")
hist(svn $Size,xlab="Size",main="Histogram of Size")
boxplot(svn $Size,ylab="Size",main="Boxplot of Size")