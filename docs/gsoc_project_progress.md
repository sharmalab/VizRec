
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

Currently, the ingestion service of VizRec accepts well-formatted JSON files as input and ingests it into the mongo database. The filtering service of VizRec generates the schema files from the database. Schema Files comprise of measures, dimensions, filter, joins, and pre-aggregations. One can visualize different chart types such as bar, pie, line, table..etc

However, the current schema-compiler of cube.dev generates very few dimensions, measures from the input data and I am looking to automate the generation with all possible combinations soon

### Presentation Slides and Demo

- **[Presentation Link](https://docs.google.com/presentation/d/1NM9nqGbIkCsfLV5yBXwJ6jOClxDYIcOevznW6aF8EQI/edit?usp=sharing)** 
- **[Demo Link](https://youtu.be/OVejQR2yszg)** 

