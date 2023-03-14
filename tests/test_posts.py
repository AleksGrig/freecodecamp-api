def test_get_all_posts(authorized_client):
    res = authorized_client.get("http://192.168.1.65/posts/")
    print(res.json())
    assert res.status_code == 200