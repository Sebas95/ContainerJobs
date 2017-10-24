import socket
import sys


ip =sys.argv[1]
print "Socket establecido con HOST1"
while True:
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect the socket to the port where the server is listening
        server_address = (ip, 10000)
        sock.connect(server_address)
        try:
               
                
                print "Ingrese la ruta de la imagen"
                ruta = raw_input("")
                sock.sendall(ruta)
                if (ruta == "salir"):
                        sock.sendall("salir")
                        break
                file = open(ruta, "rb")
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
                #message = sock.recv(100)     
                #print message
                
        finally:
            sock.close()
