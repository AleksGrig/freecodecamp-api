DESC votes;

INSERT INTO votes(user_id, post_id) values(3, 1); 

SELECT * FROM votes;

DELETE FROM votes WHERE user_id=3;