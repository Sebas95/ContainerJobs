
from PIL import Image
import numpy
import sys
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
	print pixel;

	r = pixel[0];
	g = pixel[1];
	b = pixel[2];


	if ((r>g) and (r>b)):
		print "red";
		im.save( carpR +"/" + nameOfFile)
	elif((g>r) and (g>b)):
		print "green";
		im.save( carpG +"/" + nameOfFile)
	else:
		print "blue";
		im.save( carpB +"/" + nameOfFile)


def main():
	nameOfFile =sys.argv[1];
	classifyImageInFolder(nameOfFile);


if __name__ == '__main__':
    main()