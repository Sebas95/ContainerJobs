import socket
import sys
from PIL import Image
import numpy
import os

def most_frequent_colour(image):

    w, h = image.size
    pixels = image.getcolors(w * h)

    most_frequent_pixel = pixels[0]

    for count, colour in pixels:
        if count > most_frequent_pixel[0]:
            most_frequent_pixel = (count, colour)

   

    return most_frequent_pixel

def classifyImageInFolder(nameOfFile):

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
	(cont,pixel) = most_frequent_colour(im);
	#print pixel;

	r = pixel[0];
	g = pixel[1];
	b = pixel[2];


	if ((r>g) and (r>b)):
		#print "red";
		im.save( carpR +"/" + nameOfFile)
	elif((g>r) and (g>b)):
		#print "green";
		im.save( carpG +"/" + nameOfFile)
	else:
		#print "blue";
		im.save( carpB +"/" + nameOfFile)



#------------------------ Create a TCP/IP socket-------------------
		
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
ip = socket.gethostbyname(socket.gethostname())
server_address = (ip, 10000)
print "Ip: " +ip
print "iniciando socket con HOST2"
sock.bind(server_address)

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
            name = connection.recv(1024)
            print name
            #f = open("copy_"+name, "wb")
            f = open(name, "wb")
            #print >>sys.stderr, 'connection from', client_address
            while True:
                
                data = connection.recv(1024)
                if (data == "salir"):
                    print data + "."
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
                    classifyImageInFolder(name)
                    print("Imagen procesada")
                    wait = False;
                    break;
                    
        finally:
            # Clean up the connection
            connection.close()
