#This script print the output of arp -an in output file
with open('server_ip','r') as f: #File opening in read mode, take input to output file as arp -e
    next(f) #Going to the next line (skipping the header row)
    for line in f: #Fetching content line by line
        print(line.split(' ')[0]) #Prints the first word of line