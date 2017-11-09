import socket

def get_my_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def Main():
	host = '192.168.43.130'
	port = 5001

	s = socket.socket()
	s.bind((host, port))

	s.listen(1)
	c,addr = s.accept()

	print "connection from : " + str(addr)

	while True:
		data = c.recv(1024)
		if not data:
			break
		print "client :" + str(data)

		data = raw_input('-->')
		print "sending " + str(data)
		c.send(data)
	c.close()
if __name__ == '__main__':
	Main();
