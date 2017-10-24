FROM centos:7
RUN yum install -y gcc-c++
RUN yum provides ifconfig
RUN yum install -y net-tools
RUN yum install -y libjpeg-devel
RUN yum install -y python-imaging numpy 
ADD server.c ./
ADD detector.py ./
ADD fresas.jpg ./
RUN gcc -o server server.c
EXPOSE 80/tcp
CMD ["python","detector.py","fresas.jpg"]
