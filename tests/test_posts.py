import pytest
from app import schemas


def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("http://192.168.1.65/posts/")
    posts = [schemas.PostOut(**post) for post in res.json()]
    print(posts)

    assert res.status_code == 200
    assert len(posts) == len(test_posts)


def test_unauthorized_user_get_all_posts(client, test_posts):
    res = client.get("http://192.168.1.65/posts/")
    assert res.status_code == 401


def test_unauthorized_user_get_one_post(client, test_posts):
    res = client.get(f"http://192.168.1.65/posts/{test_posts[0].id}")
    assert res.status_code == 401


def test_get_one_post_not_exist(authorized_client, test_posts):
    res = authorized_client.get("http://192.168.1.65/posts/6666")
    assert res.status_code == 404


def test_get_one_post(authorized_client, test_posts):
    res = authorized_client.get(
        f"http://192.168.1.65/posts/{test_posts[0].id}")
    post = schemas.PostOut(**res.json())
    assert res.status_code == 200
    assert post.Post.id == test_posts[0].id


@pytest.mark.parametrize("title, content, published", [
    ("awesome new title1", "awesome new content1", True),
    ("awesome new title2", "awesome new content2", True),
    ("awesome new title3", "awesome new content3", False),
])
def test_create_post(authorized_client, test_user, test_posts, title, content, published):
    res = authorized_client.post("http://192.168.1.65/posts/", json={
        "title": title,
        "content": content,
        "published": published
    })
    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == title
    assert created_post.content == content
    assert created_post.published == published
    assert created_post.owner.id == test_user['id']


def test_create_post_default_published_true(authorized_client, test_user, test_posts):
    res = authorized_client.post("http://192.168.1.65/posts/", json={
        "title": "title",
        "content": "content",
    })
    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == "title"
    assert created_post.content == "content"
    assert created_post.published == True
    assert created_post.owner.id == test_user['id']


def test_unauthorized_create_post(client, test_user, test_posts):
    res = client.post("http://192.168.1.65/posts/", json={
        "title": "title",
        "content": "content",
        "published": True
    })
    assert res.status_code == 401


def test_unauthorized_user_delete_post(client, test_user, test_posts):
    res = client.delete(f"http://192.168.1.65/posts/{test_posts[0].id}")
    assert res.status_code == 401


def test_delete_post_success(authorized_client, test_user, test_posts):
    res = authorized_client.delete(f"http://192.168.1.65/posts/{test_posts[0].id}")
    assert res.status_code == 204


def test_delete_post_not_exist(authorized_client, test_user, test_posts):
    res = authorized_client.delete("http://192.168.1.65/posts/666")
    assert res.status_code == 404


def test_delete_other_user_post(authorized_client, test_user, test_posts):
    res = authorized_client.delete(f"http://192.168.1.65/posts/{test_posts[3].id}")
    assert res.status_code == 403


def test_update_post(authorized_client, test_user, test_posts):
    data = {
        "title": "updated title",
        "content": "updated content",
        "id": test_posts[0].id
    }
    res = authorized_client.put(f"http://192.168.1.65/posts/{test_posts[0].id}", json=data)
    updated_post = schemas.Post(**res.json())
    assert res.status_code == 200
    assert updated_post.title == data["title"]
    assert updated_post.content == data["content"]