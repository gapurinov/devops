import requests
from main import simple_app

client = simple_app.test_client()

def test_response_not_empty():
    r = client.get("http://127.0.0.1:5000")
    assert r
