#!/usr/bin/env python

from socket import *
import sys
import select

host=""
port = 9999
s = socket(AF_INET,SOCK_DGRAM)
s.bind(('',port))

addr = (host,port)
buf=1024

f = open("file",'wb')

data,addr = s.recvfrom(buf)
try:
    while(data):
        f.write(data)
        s.settimeout(2)
        data,addr = s.recvfrom(buf)
except timeout:
    f.close()
    s.close()
    print "File Donwloaded"
