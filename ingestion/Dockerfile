FROM python:3.7.3-stretch

MAINTAINER Vinay
RUN apt-get update -y
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app

EXPOSE 5000
CMD ["python", "run.py"]


