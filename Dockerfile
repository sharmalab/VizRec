FROM python:3.7.3-stretch

MAINTAINER Vinay
RUN apt-get update -y
WORKDIR /inference/app
COPY requirements.txt /inference/app
RUN pip install -r /inference/app/requirements.txt
EXPOSE 5000
CMD ["python", "inference/run.py"]
