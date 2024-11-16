FROM ubuntu:24.04
RUN apt-get update && apt-get install -y python3
ADD files/hello.py /tmp
CMD [ "python3", "/tmp/hello.py" ]
