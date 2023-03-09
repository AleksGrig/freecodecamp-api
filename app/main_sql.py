from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from typing import Optional
from mysql.connector import connect
import time

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


while True:
    try:
        conn = connect(
            host="localhost",
            user="root",
            password="1234",
            database="fastapi"
        )
        cursor = conn.cursor()
        print("database connection was successful")
        break
    except Exception as error:
        print("connection to database failed")
        print("error:", error)
        time.sleep(2)

my_posts = [
    {
        "title": "title of post 1",
        "content": "content of post 1",
        "id": 1
    },
    {
        "title": "title of post 2",
        "content": "content of post 2",
        "id": 2
    }
]


def find_post(id):
    for post in my_posts:
        if post['id'] == id:
            return post


def find_post_index(id):
    for index, post in enumerate(my_posts):
        if post['id'] == id:
            return index


@app.get("/")
def root():
    return {"message": "Hello Me"}


@app.get("/posts")
def get_posts():
    cursor.execute(""" SELECT * FROM posts; """)
    posts = cursor.fetchall()
    return {"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute(
        """
      INSERT INTO posts (title, content, published)
      VALUES (%s, %s, %s)
    """,
        (post.title, post.content, post.published))
    conn.commit()
    id = cursor._last_insert_id
    cursor.execute(
        """
    SELECT * FROM posts WHERE id = %s
    """, (id,))
    new_post = cursor.fetchone()
    return {"data": new_post}


@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute(
        """
    SELECT * FROM posts WHERE id = %s 
    """, (id,)
    )
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id:{id} was not found")
    return {"post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute(
        """
    SELECT * FROM posts WHERE id = %s
    """, (id, )
    )
    post = cursor.fetchone()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id:{id} doesn't exist")

    cursor.execute(
        """
    DELETE FROM posts WHERE id = %s
    """, (id,)
    )
    conn.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute(
        """
    UPDATE posts SET title = %s, content = %s, published = %s, created_at = NOW()
    WHERE id = %s
    """, (post.title, post.content, post.published, id)
    )
    conn.commit()
    cursor.execute(
        """
    SELECT * FROM posts WHERE id = %s
    """, (id, )
    )
    updated_post = cursor.fetchone()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id:{id} doesn't exist")
    return {"data": updated_post}
