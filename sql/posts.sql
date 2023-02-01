CREATE TABLE posts_sqlalchemy (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(30) NOT NULL,
  content VARCHAR(150) NOT NULL,
  published BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMP NOT NULL DEFAULT NOW( ),
  user_id INT NOT NULL,
  FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE 
);

CREATE TABLE posts_sqlalchemy (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(30) NOT NULL,
  content VARCHAR(150) NOT NULL,
  published BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

SELECT * FROM posts;

INSERT INTO posts(title, content) VALUES
  ("first post", "interesting post"),
  ("second post", "yadayadayada");

INSERT INTO posts_sqlalchemy(title, content, owner_id) VALUES
  ("first post", "interesting post", 3),
  ("second post", "yadayadayada", 3);

DELETE FROM posts WHERE id IN (6, 7, 8)

DELETE FROM posts_sqlalchemy WHERE id = 4;

DROP TABLE posts_sqlalchemy;

DESC posts_sqlalchemy;

SELECT * FROM posts_sqlalchemy;

DELETE FROM posts_sqlalchemy;

ALTER TABLE posts_sqlalchemy 
ADD user_id INT NOT NULL;

ALTER TABLE posts_sqlalchemy DROP COLUMN user_id;

ALTER TABLE posts_sqlalchemy
ADD FOREIGN KEY(user_id) REFERENCES users(id) ;

ALTER TABLE posts_sqlalchemy
DROP FOREIGN KEY user_id;

