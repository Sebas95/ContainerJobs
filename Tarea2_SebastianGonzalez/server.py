import socket
import sys
from PIL import Image
import numpy
import os
import shutil 

def most_frequent_colour(image):

    w, h = image.size
    pixels = image.getcolors(w * h)

    most_frequent_pixel = pixels[0]

    for count, colour in pixels:
        if count > most_frequent_pixel[0]:
            most_frequent_pixel = (count, colour)
    return most_frequent_pixel


def validarIp(ip_connected):
	
	file = open("carpetaDocker/configuracion.config", "r") 
	lista_ips = file.readlines() 
	for ip in lista_ips:
		if ((ip_connected[0]+ "\n" ) == ip):
			return True	
	return False

def classifyImageInFolder(nameOfFile,client_address):
	
    	if(not(nameOfFile == "salirsalir")):

		if not os.path.exists("carpetaDocker/container1"):
			os.makedirs("carpetaDocker/container1");
	
		carpR= "carpetaDocker/container1/R";
		carpG= "carpetaDocker/container1/G";
		carpB= "carpetaDocker/container1/B";
		carpN= "carpetaDocker/container1/not_trusted";
		if not os.path.exists(carpR):
			os.makedirs(carpR);
		if not os.path.exists(carpG):
			os.makedirs(carpG);
		if not os.path.exists(carpB):
			os.makedirs(carpB);
		if not os.path.exists(carpN):
			os.makedirs(carpN);

		im = Image.open(nameOfFile);
		valid = validarIp(client_address)
		if (valid == True):
			
			(cont,pixel) = most_frequent_colour(im);
		

			r = pixel[0];
			g = pixel[1];
			b = pixel[2];	
			
			if ((r>g) and (r>b)):
				im.save( carpR +"/" + nameOfFile)
			elif((g>r) and (g>b)):
				im.save( carpG +"/" + nameOfFile)
			else:
				im.save( carpB +"/" + nameOfFile)
			return True

		else:
			
			im.save( carpN +"/" + nameOfFile)
			return False
	 

#------------------------ Create a TCP/IP socket-------------------
		
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('0.0.0.0', 10000)
print "iniciando socket con HOST2"
sock.bind(server_address)
if (os.path.exists("carpetaDocker/configuracion.config")):
	os.remove("carpetaDocker/configuracion.config")
shutil.move("configuracion.config", "carpetaDocker")
# Listen for incoming connections
sock.listen(1)
serverRun = True

while serverRun:
    wait = True
        
    # Wait for a connection
    connection, client_address = sock.accept()
    #print >>sys.stderr, 'waiting for a connection'
    while wait == True:  
        try:
            ruta = connection.recv(1024)
	    ruta2 = ruta
            lista = ruta2.split("/")
	    name = lista[len(lista)-1]
            f = open(name, "wb")
            #print >>sys.stderr, 'connection from', client_address
            while True:
                
                data = connection.recv(1024)
		
                if (ruta == "salirsalir"):
                    serverRun = False
                    wait = False;
                    break
                elif data:
                    f.write(data)
                else:
                    #print >>sys.stderr, 'Imagen recibida', client_address
                    print 'Imagen recibida'
                    connection.send("listo")
                    f.close()
                    #enviar a las capertas-------
                    procesed = classifyImageInFolder(name,client_address)
		    if (procesed):
                    	print("Imagen procesada")
		    else: 
			print("Imagen No procesada")
                    wait = False;
                    break;
                    
        finally:
            # Clean up the connection
            connection.close()

print("host 2 desconectado")
