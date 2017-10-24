import socket
import sys
from PIL import Image
import numpy

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 10011)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
# Recibe los datos en trozos y reetransmite
bandera = False
while True:
    bandera = False
    f = open("/home/sebastian95/Documents/GitHub/ContainerJobs/nuevo.jpg", "wb")
    # Wait for a connection
    connection, client_address = sock.accept()
    print >>sys.stderr, 'waiting for a connection'
    while bandera == False:  
        try:
            print >>sys.stderr, 'connection from', client_address
            while True:
                data = connection.recv(1024)
                
                if data:
                    f.write(data)
                else:
                    print >>sys.stderr, 'Imagen recibida', client_address
                    connection.send("listo")
                    f.close()
                    
                    print("termino la conexion")
                    bandera = True;
                    break;
                    
        finally:
            # Clean up the connection
            connection.close()
