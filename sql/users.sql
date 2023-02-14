INSERT INTO users(email, password) VALUES("test1@gmail.com", "test1_password");

DESC users;

DROP TABLE users;

SELECT * FROM users;

DELETE FROM users WHERE id = 6;

DELETE FROM alembic_version WHERE version_num='de0d647c3291'
