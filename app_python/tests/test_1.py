import requests


def test_response_code(client):
    r = requests.get("http://127.0.0.1:5000")
    assert r.status_code == 200
