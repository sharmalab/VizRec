
# Deep Learning Guided Visual Exploration of Data 

 [![CircleCI](https://circleci.com/gh/sharmalab/VizRec.svg?style=svg)](https://circleci.com/gh/sharmalab/VizRec) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![HitCount](http://hits.dwyl.io/sharmalab/https://githubcom/sharmalab/VizRec.svg)](http://hits.dwyl.io/sharmalab/https://githubcom/sharmalab/VizRec)

## Description

VizRec recommends visualizations that are more interesting and efficient with the Deep Learning Models on well formatted input data.

## Quickstart Guide


- Without running containers

```
git clone https://github.com/sharmalab/VizRec.git
pip install -r requirements.txt
cd VizRec 
python3 ingestion/run.py
cd query/
sudo npm install
```
- Update `.env` from *[docs](https://cube.dev/docs/connecting-to-the-database#configuring-connection-for-cube-js-cli-created-apps)*

```
sudo npm run dev


```
- Download **[mongo connector](https://www.mongodb.com/download-center/bi-connector)** and run `bin/mongosqld` to run queries with sql 



- With containers

```
git clone https://github.com/sharmalab/VizRec.git
docker-compose build
docker-compose up
```


## Contributing

Feel free to send pull requests or report any issues. We'll be glad to incorporate meaningful ones 

## License

This project is licensed under **[Apache 2.0 License](https://github.com/sharmalab/VizRec/blob/master/LICENSE.md)** 
