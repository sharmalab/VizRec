FROM python:3.7.3-stretch

MAINTAINER Vinay
RUN apt-get update -y
COPY requirements.txt /inference/app/requirements.txt
WORKDIR /inference/app
RUN pip install -r requirements.txt
COPY . /inference/app

EXPOSE 5000
CMD ["python", "inference/run.py"]
