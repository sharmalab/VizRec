import json
from app import app


def test_uploadfile():
    client = app.test_client()
    response = client.post("/upload_file", data=json.dumps(dict(f='f')))
    assert response.status_code == 200
