FROM ubuntu:24.04
RUN apt-get update && apt-get install -y python3
WORKDIR /work
COPY files/hello.py /work
CMD [ "python3", "/work/hello.py" ]
