#!/usr/bin/python

from random import randint
from socket import *
import sys
import select
import subprocess

def random_with_N_digits(n):			#Function for printing random no.'s
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def OSinfo(thisisit):					# OSinfo function returns 0 on success
    try:
        osstdout = subprocess.call(thisisit.split())
    except subprocess.CalledProcessError:
        return 1
    return osstdout

host=""
port = 9999								#Port being used by server
s = socket(AF_INET,SOCK_DGRAM)
s.bind(('',port))

addr = (host,port)
buf=1024								#Buffer size

#file = random_with_N_digits(4)

f = open("files/file.txt",'wb')			#Opening file in write mode
data,addr = s.recvfrom(buf)
try:
    while(data):
        f.write(data)
        s.settimeout(2)
        data,addr = s.recvfrom(buf)
except timeout:
    f.close()							#Closing the opened file
    s.close()							#Closing the socket connection
print("File Downloaded")


filepath = "files/file.txt" 			#Path to file having commands. Every line has only one command 
with open(filepath) as fp:  
   line = fp.readline()
   cnt = 1
   array = []
   while line:
       print("Line {}: {}".format(cnt, line.strip())) # Print which line and command is executing
       j = OSinfo(line)   				#j is status returned by OSinfo
       array.append(j)
       line = fp.readline()
       cnt += 1

print(array) 							#Prints all the statuses
