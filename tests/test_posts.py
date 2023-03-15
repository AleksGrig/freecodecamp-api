from typing import List
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