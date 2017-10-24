import socket
import sys


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10004)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
        file = open("/home/sebastian95/Documents/GitHub/ContainerJobs/fresas.jpg", "rb")
	# Send data
	content = file.read(1024)
	while True:
                if content:
                        sock.sendall(content)
                        content = file.read(1024)
                else:
                        print ("yamomo")
                        break
                
        print ("yamomo2")       
        sock.sendall(chr(1))
        print ("yamomo3")       
        file.close()    
	data = sock.recv(100)
	print ("yamomo4")       
	print data
#except IOError as e:
 #   if e.errno == errno.EPIPE:
  #      print "error"
finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
