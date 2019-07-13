FROM node:10-alpine

WORKDIR /VizRec/query

COPY package*.json ./

RUN npm install

COPY . /VizRec/query

EXPOSE 8000

