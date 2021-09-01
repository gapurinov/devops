import requests


def test_response_not_empty(client):
    r = requests.get("http://127.0.0.1:5000")
    assert r.content
