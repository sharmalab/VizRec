# [VizRec System Architecture]

* Status: [proposed] 
* Deciders: [Ganesh Iyer, Vinay Pandramish] 
* Date: [2019-05-28]

Technical Story: [https://github.com/sharmalab/VizRec/issues/19]

## Context and Problem Statement

[Come up deep learning models that do a visual exploration of data.The architecture with different components and dotted ones are serverless]

## Decision Drivers <!-- optional -->

* [Input - Well formated json]
* [VizRecDB - It could be Postgres/Mongo]
* [Data Ingestion - Flask/Python microservices]
* [Data Filtering - Flask/Python microservices]
* [Data Inference - Flask/Python Microservices]
* [Model Registry - Docker Container]
* [Vega Lite Specification - Output of Machine Learning Models]
* [Vega Lite Rendering - React+JS+Vega Lite for Rendering]

## Considered Options

* [Amazon SageMaker]
* [Cloud Native Microservices Architectures]

## Decision Outcome

Chosen option: "[Cloud Native Microservices Architecture]", because we prefer cloud vendor agnostic ones for the design

### Positive Consequences <!-- optional -->

* [Economics]

---

#### Design

![Design](_static/system_architecture.png)

---
