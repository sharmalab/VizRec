import json
from app.inference import app


def test_uploadfile():
    client = app.test_client()
    response = client.post("/upload_file", data=json.dumps(dict(f='f')))
    assert response.status_code == 400
    response1 = client.get("/upload_file", data=json.dumps(dict(f='f')))
    assert response1.status_code == 405
