FROM node:10-alpine

WORKDIR /query

COPY package*.json /query/

RUN npm install

COPY . /query

EXPOSE 4000

