FROM ubuntu:16.04

MAINTAINER Vinay
RUN apt-get update -y && \
   apt-get install -y python3-dev python3-pip
WORKDIR /inference/app
COPY . /inference/app
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["inference/run.py"]
