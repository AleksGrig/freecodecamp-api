DESC votes;

INSERT INTO votes(user_id, post_id) values
(8, 1),
(3, 4); 

SELECT * FROM votes;

SELECT posts.*, COUNT(votes.post_id) FROM posts LEFT JOIN votes ON posts.id=votes.post_id GROUP BY posts.id;

DELETE FROM votes WHERE user_id=3;

DROP TABLE votes;