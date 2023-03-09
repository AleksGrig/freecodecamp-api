import requests
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import schemas
from app.config import settings 
from app.main import app
from app.database import get_db
from app.models import Base


SQLALCHEMY_DATABASE_URL = f'mysql://root:1234@192.168.1.65:3306/fastapi_test'
# SQLALCHEMY_DATABASE_URL = f'mysql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
  db = TestingSessionLocal()
  try:
    yield db
  finally:
    db.close()

app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def client():
  # run our code before out test
  Base.metadata.drop_all(bind=engine)
  Base.metadata.create_all(bind=engine)

  yield TestClient(app)

  # run our code after test finishes
   

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