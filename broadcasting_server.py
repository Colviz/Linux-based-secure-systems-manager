#!/usr/bin/python

import sys
from socket import *
cs = socket(AF_INET, SOCK_DGRAM)
cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

port = 9999                             #Port in use
addr = ('255.255.255.255',port)         #Address used for broadcasting

buf =1024                               #Buffer Size
file_name=sys.argv[1]                   #Taking file name from command line argument [0]-program_file name, [1]- input provided

f=open(file_name,"rb")                  #Opening file in read mode 
data = f.read(buf)                      #Taking the data from file into data variable

cs.sendto(data,addr)                    #Sending data to the broadcasting address
while (data):
  if(cs.sendto(data,addr)):
    print("Sending File...")
    data = f.read(buf)
f.close()                               #Closing the opened file
cs.close()                              #Closing the socket connection
