# Vince
> There can be discrepencies in the content provided below.

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

## Try -
> Implement these things for better understanding of the project.
1. Chat server (single client & multiple clients/group chat).
2. Data transfer (single client & multiple clients/multicasting).
3. Code and Data - Transport both as payload (single client & multiple clients).

## Useful links to refer -
* [Sockets - Python 3.4](https://docs.python.org/3.4/howto/sockets.html)
* [Sockets - Python 2.7](https://docs.python.org/2.7/library/socket.html)
* [Sockets - Python Tips](https://pythontips.com/2013/08/06/python-socket-network-programming/)
* [Python networking - tutorialspoint](https://www.tutorialspoint.com/python/python_networking.htm)

## Extra links -
* [Network Administrator Tools](http://www.networkmanagementsoftware.com/top-17-free-tools-for-network-administrators/)
* [nmap](https://nmap.org/)
* [angryip](http://angryip.org/)
* [ntop](http://www.ntop.org/)

## Presentation -
* Slide 1 - Vince (ie. name of project)
* Slide 2 - What is Vince?
  * Its an autonomous entity.
  * Will be used to manage computers in a subnet.
  
* Slide 3 - Working of Vince.
  * Checks no. of live systems & gets their IP.
  * Establish connection with hosts (underway).
  * Sends payload using UDP.
    * payload - | Payload 1 (Shell Script) | Playlod 2 (Data file)|
  * Sends response code.

* Slide 4 - Main components it targets.
  * IP range
  * Sockets
  * Shell scripts
  * Responses

* Slide 5 - Is data transmission secure in Vince?
  * Can use asymmetric encryption & encrypt data and payload before sending.

* Slide 6 - Advantages and limitaions.
  * Easy management and hence utilization of resources.
  * Flexible enough to transfer data securily.
  
  * Only for subnets.
  * It requires credentials.
  
* Slide 7 - Thank You (Name of Team members, roll no. wise)
