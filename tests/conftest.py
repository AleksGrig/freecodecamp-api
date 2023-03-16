import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import schemas, models
from app.config import settings
from app.main import app
from app.database import get_db
from app.models import Base
from app.oauth2 import create_access_token


SQLALCHEMY_DATABASE_URL = 'mysql://root:1234@192.168.1.65:3306/fastapi_test'
SQLALCHEMY_DATABASE_URL_LOCALHOST = 'mysql://root:1234@localhost:3306/fastapi_test'
# SQLALCHEMY_DATABASE_URL = f'mysql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'
engine = create_engine(SQLALCHEMY_DATABASE_URL_LOCALHOST)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def client(session):
    # run our code before out test
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)

    # run our code after test finishes


@pytest.fixture
def test_user(client):
    userdata = {
        "email": "hello123@gmail.com",
        "password": "hello123"
    }
    res = client.post("/users/", json=userdata)
    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = userdata['password']
    return new_user


@pytest.fixture
def test_user2(client):
    userdata = {
        "email": "hello234@gmail.com",
        "password": "hello234"
    }
    res = client.post("/users/", json=userdata)
    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = userdata['password']
    return new_user


@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user['id']})


@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }
    return client


@pytest.fixture
def test_posts(test_user, test_user2, session):
    posts_data = [
        {
            "title": "first_title",
            "content": "first_content",
            "owner_id": test_user['id']
        },
        {
            "title": "2nd_title",
            "content": "2nd_content",
            "owner_id": test_user['id']
        },
        {
            "title": "3rd_title",
            "content": "3rd_content",
            "owner_id": test_user['id']
        },
        {
            "title": "4th_title",
            "content": "4th_content",
            "owner_id": test_user2['id']
        },
    ]
    posts = [models.Post(**post_data) for post_data in posts_data]
    session.add_all(posts)
    session.commit()

    posts = session.query(models.Post).all()
    return posts
