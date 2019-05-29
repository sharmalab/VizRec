from app import app


def test_upload():
    client = app.test_client()
    rsp = client.get('/upload_file')
    html = rsp.get_data(as_text=True)
    assert '<h1>Upload json</h1>' in html