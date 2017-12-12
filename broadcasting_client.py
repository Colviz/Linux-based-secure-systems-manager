#!/usr/bin/python

from random import randint
from socket import *
import sys
import select
import subprocess

#Executing command on system
def OSinfo(thisisit):         # OSinfo function returns 0 on success
    try:
        osstdout = subprocess.call(thisisit.split())
    except subprocess.CalledProcessError:
        return 1
    return osstdout

host=""
port = 9999           #Port being used by server
s = socket(AF_INET,SOCK_DGRAM)
s.bind(('',port))

addr = (host,port)
buf=1024                #Buffer size

#Writing the received data to file
file = "file.txt"       #Name of file
f = open(file,'wb')             #Opening file in write mode
data,addr = s.recvfrom(buf)
try:
    while(data):
        f.write(data)
        #print(data)
        s.settimeout(2)
        data,addr = s.recvfrom(buf)
except timeout:
    f.close()           #Closing the opened file
    s.close()           #Closing the socket connection
print("File Downloaded\n")

#Getting no. of lines in file
num_lines = sum(1 for line in open(file,'r'))
print("No. of commands in file are : ") 
print(num_lines)          #Printing no. of lines
num_lines = num_lines-1
#Commands in file and server IP
print("List of commands and server IP :")
a = open(file,'r')
file_contents = a.read()
print(file_contents)
a.close()

#Executing all the commands one by one
with open(file) as fp:  
   line = fp.readline()
   cnt = 1
   array = []
   while num_lines:
       print("Line {}: {}".format(cnt, line.strip()))   #Print which line and command is executing
       j = OSinfo(line)           #j is status returned by OSinfo
       array.append(j)
       num_lines -= 1
       line = fp.readline()
       cnt += 1

print(array)            #Prints all the statuses
