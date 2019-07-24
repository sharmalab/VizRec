import json
from app.ingest import app
import os
import glob
from flask.debughelpers import DebugFilesKeyError


def test_uploadfile():
    client = app.test_client()
    response = client.post("/upload_file", data=json.dumps(dict(f='f')))
    assert response.status_code == 400
    response1 = client.get("/upload_file", data=json.dumps(dict(f='f')))
    assert response1.status_code == 405
    valids = ["json"]
    data = dict()
    data['file'] = '../query/examples/Zips/zips.json'
    assert(glob.glob(os.getcwd() + '/**/' + data['file'], recursive=True))
    assert(data['file'].split('/')[-1].split('.')[1] in valids)
    try:
        client.post('/upload_file', data=data)
    except DebugFilesKeyError as e:
        print(e)
