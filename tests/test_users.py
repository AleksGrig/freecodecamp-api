from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_root():
    res = client.get("http://192.168.1.65/")
    assert res.json().get('message') == 'my fastapi'
    assert res.status_code == 200