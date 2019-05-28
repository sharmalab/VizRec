from io import StringIO, BytesIO
from app import app


def test_upload():
    client = app.test_client()
    rsp = client.get('/upload_file')
    assert rsp.status == '200 OK'
    html = rsp.get_data(as_text=True)
    assert '<h1>Upload json</h1>' in html
    response = client.get("/upload_file")
    assert response.status_code == 200
    
