#!/usr/bin/python

from subprocess import call
import sys
import os
from socket import *
cs = socket(AF_INET, SOCK_DGRAM)
cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

###Broadcast according to client group
#Show ports associated with a particular group
file = "group_port.txt"       #Name of file containing Groups
a = open(file,'r')
file_contents = a.read()
print(file_contents)
a.close()

#Taking port as input
print("Enter the port of the associated Group: ")
port = int(input())

###Assigning the port and broadcasting address 
#Note - Change Port no. according to the group no.
#port = 9999                             #Default port
addr = ('255.255.255.255',port)         #Address used for broadcasting


###Setting the buffer size
buf =1024                               #Buffer Size
file_name=sys.argv[1]                   #Taking file name from command line argument [0]-program_file name, [1]- input provided
                                        #[2] - multicast (using for broadcasting), [3] - file with list of IP's,on which to broadcast

###Writing server's IP to file

#Taking the ip as input from server_ip file - just for reference
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

#Encrypting the file with GPG key
call(["gpg", "-r", "trialuser@mailinator.com", "-e", file_name])
file_name = file_name+".gpg"            #New file name


###Putting the file's content in buffer
f=open(file_name,"rb")                  #Opening file in read mode 
data = f.read(buf)                      #Taking the data from file into data variable

###Sending the data
print("##################################################")
print("#                 Sending File...                #")
print("##################################################\n")
print("##################################################")
print("#                   File sent                    #")
print("##################################################")
os.remove(file_name)                    #Delete the intermediate (encrypted file)
cs.sendto(data,addr)                    #Sending data to the broadcasting address
#The code below was responsible for all the errors during execution
'''while (data):
  #if(cs.sendto(data,addr)):
  if(cs.sendto(data,(addr,port))):
    print("Sending File...")
    data = f.read(buf)
f.close()                               #Closing the opened file
cs.close()                              #Closing the socket connection
'''