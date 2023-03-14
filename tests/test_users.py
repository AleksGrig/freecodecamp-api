import requests
import pytest
from jose import jwt 
from app import schemas, config
from .database import client, session


@pytest.fixture
def test_user(client):
    userdata = {
        "email": "hello123@gmail.com",
        "password": "hello123"
    }
    res = client.post("http://192.168.1.65/users/", json=userdata)
    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = userdata['password']
    return new_user


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


# we send credentials using form-data, not json!!!
def test_login_user(client, test_user):
    res = client.post("/login", data={
        "username": test_user['email'],
        "password": test_user['password']
    })
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, config.settings.secret_key, algorithms=[config.settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == 'bearer'
    assert res.status_code == 200
