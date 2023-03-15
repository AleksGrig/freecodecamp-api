def test_vote_on_post(authorized_client, test_posts):
    res = authorized_client.post("http://192.168.1.65/vote/", json={
        "post_id": test_posts[0].id,
        "dir": 1
    })
    assert res.status_code == 201
