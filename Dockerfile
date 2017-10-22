FROM centos:7
RUN yum install -y gcc-c++
RUN yum provides ifconfig
RUN yum install -y net-tools
RUN ls
ADD index.html ./
ADD server.c ./
RUN gcc -o server server.c
EXPOSE 80/tcp
CMD ["./server"]
