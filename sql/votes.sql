DESC votes;

INSERT INTO votes(user_id, post_id) values(3, 1); 

SELECT * FROM votes;

SELECT posts_sqlalchemy.*, COUNT(votes.post_id) FROM posts_sqlalchemy LEFT JOIN votes ON posts_sqlalchemy.id=votes.post_id GROUP BY posts_sqlalchemy.id;

DELETE FROM votes WHERE user_id=3;