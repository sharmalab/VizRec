FROM python:3.7.3-stretch

MAINTAINER Vinay
RUN apt-get update -y
COPY requirements.txt /ingestion/app/requirements.txt
WORKDIR /ingestion/app
RUN pip install -r requirements.txt
COPY . /ingestion/app

EXPOSE 5000
CMD ["python", "ingestion/run.py"]
