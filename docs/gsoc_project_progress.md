
# Deep Learning Guided Visual Exploration of data

This document is about the progress of the Project during Phase-II for Google Summer of Code - GSoC 2019

## Overview

VizRec takes a well formatted input data and suggest visualizations that could be more efficient and interesting with the aid of Deep Learning Models.

These are the list of tasks accomplished so far from the **[system architecture](_static/system_architecture.png)**

## Tasks

- Setting Up Continuos Integration
- Coming up With System Architecture
- Data Ingestion Service
- Data Filtering Service
- Containerizing Ingestion and Filtering Service
- Semi-Parser(Generates Measures)

## Description

Currently,VizRec takes selected json files and ingests it into the mongo database . From the database, the filtering service generates the schema files that can be used to have different chart types like bar,pie,line,table..etc.However it can generate a fewer parameters currently because of the limited number of aggregates and measures enabled in the schema compiler of cube.dev and are looking to automate it in the future


### Presentation Slides and Demo

- **[Presentation Link](https://docs.google.com/presentation/d/1NM9nqGbIkCsfLV5yBXwJ6jOClxDYIcOevznW6aF8EQI/edit?usp=sharing)** 
- **[Demo Link](https://youtu.be/OVejQR2yszg)** 

