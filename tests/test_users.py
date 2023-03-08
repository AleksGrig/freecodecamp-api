import requests
from app import schemas


def test_root():
    res = requests.get("http://192.168.1.65/")
    assert res.json().get('message') == 'my fastapi'
    assert res.status_code == 200

def test_create_user():
    res = requests.post("http://192.168.1.65/users/", json={
        "email": "hello123@gmail.com",
        "password": "hello123"
    })
    print(res.json())
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "hello123@gmail.com"
    assert res.status_code == 201