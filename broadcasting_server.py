#!/usr/bin/python

from socket import *
cs = socket(AF_INET, SOCK_DGRAM)
cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

port = 9999
addr = ('255.255.255.255',port)

buf =1024
file_name='temp.txt'

f=open(file_name,"rb") 
data = f.read(buf)

cs.sendto(data,addr)
while (data):
    if(cs.sendto(data,addr)):
        print "sending ..."
        data = f.read(buf)
cs.close()
f.close()

