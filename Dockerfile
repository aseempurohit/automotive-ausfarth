FROM ubuntu:16.04
MAINTAINER Anderson Miller <anderson.miller@frogdesign.com>

RUN echo "8.8.8.8" >> /etc/resolv.conf
RUN echo "8.8.4.4" >> /etc/resolv.conf
RUN apt-get update
RUN apt-get install -y python
RUN mkdir /frog
COPY . /frog/
WORKDIR /frog/

CMD ["/usr/bin/python","car_server.py"]
EXPOSE 50024

