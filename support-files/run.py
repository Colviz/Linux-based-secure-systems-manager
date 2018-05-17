import subprocess

# OSinfo function return 0 if successful otherwise return 1 if error accure
def OSinfo(runthis):
        try:
            osstdout = subprocess.check_call(runthis.split())
        except subprocess.CalledProcessError:
            return 1
        return osstdout


filepath = 'commands.txt' # commands.txt file have commands. Every line has only one command 
with open(filepath) as fp:  
   line = fp.readline()
   cnt = 1
   array = []
   while line:
       print("Line {}: {}".format(cnt, line.strip())) # Print which line and command is executing
       s = OSinfo(line)    # s is status returned by OSinfo
       array.append(s)
       line = fp.readline()
       cnt += 1

print(array) # print all status in serial