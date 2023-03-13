import requests
from app import schemas
from .database import client, session

def test_root(client):
    # res = requests.get("http://192.168.1.65/")
    res = client.get("http://192.168.1.65/")
    assert res.json().get('message') == 'my fastapi'
    assert res.status_code == 200


def test_create_user(client):
    # res = requests.post("http://192.168.1.65/users/", json={
    #     "email": "hello123@gmail.com",
    #     "password": "hello123"
    # })
    res = client.post("http://192.168.1.65/users/", json={
        "email": "hello123@gmail.com",
        "password": "hello123"
    })
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "hello123@gmail.com"
    assert res.status_code == 201
