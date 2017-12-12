#!/usr/bin/python

import sys
from socket import *
cs = socket(AF_INET, SOCK_DGRAM)
cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

###Assigning the port and broadcasting address
port = 9999                             #Port in use
addr = ('255.255.255.255',port)         #Address used for broadcasting

###Setting the buffer size
buf =1024                               #Buffer Size
file_name=sys.argv[1]                   #Taking file name from command line argument [0]-program_file name, [1]- input provided

###Writing server's IP to file

#Taking the ip as input from server_ip file
fp = open("server_ip","r")
ip = fp.read()
fp.close()

written = 0
ipp = ip

#Checking if IP already exists
fl = open(file_name,'r')
lines = fl.readlines()
for line in lines:
  if line == ipp:
    written = 1
fl.close()

#If not written then write IP to file
if written !=1:
	file = open(file_name,"a") 
	file.write(ip) 
	file.close() 
#Writing IP ends here

###Putting the file's content in buffer

f=open(file_name,"rb")                  #Opening file in read mode 
data = f.read(buf)                      #Taking the data from file into data variable

###Sending the data
print("Sending File...")
print("File sent\n")
cs.sendto(data,addr)                    #Sending data to the broadcasting address
while (data):
  #if(cs.sendto(data,addr)):
  if(cs.sendto(data,(addr,port))):
    print("Sending File...")
    data = f.read(buf)
f.close()                               #Closing the opened file
cs.close()                              #Closing the socket connection
print("File sent")
