CREATE TABLE posts (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(30) NOT NULL,
  content VARCHAR(150) NOT NULL,
  published BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMP NOT NULL DEFAULT NOW( ),
  user_id INT NOT NULL,
  FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE 
);

CREATE TABLE posts (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(30) NOT NULL,
  content VARCHAR(150) NOT NULL,
  published BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

DESC posts;

DROP TABLE posts;

SELECT * FROM posts;

INSERT INTO posts(title, content, owner_id) VALUES
  ("first post ", "interesting post", 3),
  ("second post", "yadayadayada", 3),
  ("third post", "best post", 3),
  ("second user", "my post", 7),
  ("second user post 2", "new post", 7),
  ("third user post 1", "first post", 8);

DELETE FROM posts WHERE id IN (6, 7, 8)

DELETE FROM posts WHERE id = 4;

DROP TABLE posts;

DROP COLUMN content FROM posts;

SELECT * FROM posts LEFT JOIN users ON posts.owner_id=users.id;

SELECT users.id, COUNT(posts.id) FROM posts RIGHT JOIN users ON posts.owner_id=users.id GROUP BY users.id;

DELETE FROM posts;

ALTER TABLE posts 
ADD user_id INT NOT NULL;

ALTER TABLE posts DROP COLUMN user_id;

ALTER TABLE posts
ADD FOREIGN KEY(user_id) REFERENCES users(id) ;

ALTER TABLE posts
DROP FOREIGN KEY user_id;

