import socket
import sys
from PIL import Image
import numpy

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 10011)
#print >>sys.stderr, 'starting up on %s port %s' % server_address
print "iniciando socket con HOST2"
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
serverRun = True
while serverRun:
    wait = True
    f = open("/home/sebastian95/Documents/GitHub/ContainerJobs/nuevo.jpg", "wb")
    # Wait for a connection
    connection, client_address = sock.accept()
    #print >>sys.stderr, 'waiting for a connection'
    while wait == True:  
        try:
            #print >>sys.stderr, 'connection from', client_address
            while True:
                data = connection.recv(1024)
                if data:
                    f.write(data)
                else:
                    #print >>sys.stderr, 'Imagen recibida', client_address
                    print 'Imagen recibida'
                    connection.send("listo")
                    f.close()
                    #enviar a las capertas-------
                    print("Imagen procesada")
                    wait = False;
                    break;
                    
        finally:
            # Clean up the connection
            connection.close()
