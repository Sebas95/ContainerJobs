import socket
import sys

print "Socket establecido con HOST1"
while True:
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect the socket to the port where the server is listening
        server_address = ('localhost', 10011)
        sock.connect(server_address)
        try:
               
                
                print "Ingrese la ruta de la imagen"
                ruta = raw_input("")
                if (ruta == "salir"):
                        break
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
                
                file.close()
                        #data = sock.recv(100)     
                        #print data
                #except IOError as e:
                 #   if e.errno == errno.EPIPE:
                  #      print "error"
        finally:
            sock.close()
