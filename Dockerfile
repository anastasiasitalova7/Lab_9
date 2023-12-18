FROM ubuntu

RUN apt update
RUN apt install python3 python3-pip -y

RUN pip3 install flask

COPY . /Project

CMD python3 /Project/my.py
