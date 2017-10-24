import socket
import sys


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = ('localhost', 10011)
sock.connect(server_address)
try:
       
                print "Socket establecido con HOST1"
                print "Ingrese la ruta de la imagen"
                ruta = raw_input("")
                file = open("/home/sebastian95/Documents/GitHub/ContainerJobs/forest.jpg", "rb")
                # Send data
                content = file.read(1024)
                while True:
                        if content:
                                sock.sendall(content)
                                content = file.read(1024)
                        else:
                                print "Enviando imagen ........"
                                break
                             
                print "Imagen enviada"
                sock.sendall("g")
                file.close()
                #data = sock.recv(100)     
                #print data
        #except IOError as e:
         #   if e.errno == errno.EPIPE:
          #      print "error"
finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
