# Vince
> In development phase.
> There can be discrepencies in the content provided below.
> Please refer **learning** branch.

## Main Components to consider -
> Just for reference (not sure about their accuracy)
1. Search whether any existing such software exists?
2. What will our agent do?
3. How will it work?
4. What components will it target while working?
5. How is it different from rest of the softwares?
6. How is it secure & reliable, as compared to others?
7. Advantages & limitations.
8. Is there any stable software that can pass our call through any system reserved port rather than above 1024 ports.

## Roadmap -
### Requirements -
1. Server side (Mobile agent)
2. Client side (script installed in system)

### Working of server side script -
* payload - | Payload 1 (Shell Script/Code) | Playlod 2 (Data file)|

### Working of client side script - 
* takes payload 1 into consideration and then will execute accordingly.

## Installing the client (using shebang)
Walkthrough of making a python script available anywhere:

Make a python script:
```
cd /home/el/bin
touch stuff.py
chmod +x stuff.py
```
Find out where your python is:

which python
``/usr/bin/python``

Put this code in there:

```
#!/usr/bin/python
print "hi"
```
Run in it the same directory:

``python stuff.py``

Go up a directory and it's not available:
```
cd ..
stuff.py

-bash: stuff.py: command not found
```
Not found! It's as we expect, add the file path of the python file to the $PATH

``vi ~/.bashrc``

Add the file:

``export PATH=$PATH:/home/el/bin``

Save it out, re apply the .bashrc, and retry

``source ~/.bashrc``

Try again:
```
cd /home/el
stuff.py
```
Prints:

``hi``

The trick is that the bash shell knows the language of the file via the shebang.

## Try -
> Implement these things for better understanding of the project.
1. Chat server (single client & multiple clients/group chat).
2. Data transfer (single client & multiple clients/multicasting).
3. Code and Data - Transport both as payload (single client & multiple clients).

## Useful links to refer -
* [Important - UDP Communicatios](https://wiki.python.org/moin/UdpCommunication)
* [Sockets - Python 3.4](https://docs.python.org/3.4/howto/sockets.html)
* [Sockets - Python 2.7](https://docs.python.org/2.7/library/socket.html)
* [Sockets - Python Tips](https://pythontips.com/2013/08/06/python-socket-network-programming/)
* [Python networking - tutorialspoint](https://www.tutorialspoint.com/python/python_networking.htm)

## Extra links -
* [Network Administrator Tools](http://www.networkmanagementsoftware.com/top-17-free-tools-for-network-administrators/)
* [nmap](https://nmap.org/)
* [angryip](http://angryip.org/)
* [ntop](http://www.ntop.org/)

## Running the project

* For running the client script
```
	python broadcasting_client.py
```
Note - ``client`` will save the received file to ``files/file.txt``.

* For running the server script (it requires input file)
```
	python broadcasting_server.py temp.txt
```
Note - ``temp.txt`` holds all the commands that needs to be executed on the clients.

###  Generating a GPG key
* For generating a GPG key refer [here](https://help.github.com/articles/generating-a-new-gpg-key/)
* Documentation regarding GPG is [here](https://pythonhosted.org/gnupg/gnupg.html)