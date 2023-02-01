CREATE database fastapi;

USE fastapi;

CREATE TABLE products (
  name VARCHAR(30) NOT NULL,
  price INT not NULL,
  id INT AUTO_INCREMENT PRIMARY KEY
);

CREATE TABLE products (
  name VARCHAR(30) NOT NULL,
  price INT not NULL,
  id INT AUTO_INCREMENT PRIMARY KEY,
  on_sale BOOLEAN NOT NULL DEFAULT FALSE,
  inventory INT NOT NULL DEFAULT 0,
  created_at DATETIME NOT NULL DEFAULT NOW()
);

INSERT INTO products(name, price) VALUES("iphone se", 250);

INSERT INTO products(name, price, inventory) VALUES
  ("iphone XR", 500, 200),
  ("iphone 12 mini", 700, 230);

INSERT INTO products(name, price, inventory) VALUES
  ("iphone se", 250, 120),
  ("iphone 7", 300, 400),
  ("iphone 8", 350, 300),
  ("iphone 12 pro max", 900, 370),
  ("iphone 13 pro max", 1100, 160);

UPDATE products
SET on_sale = TRUE
WHERE id IN (14, 17, 19);

ALTER TABLE products
ADD on_sale BOOLEAN DEFAULT FALSE;

ALTER TABLE products
ADD inventory INT DEFAULT 0;

DESCRIBE products;

ALTER TABLE products
MODIFY on_sale BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE products
MODIFY inventory INT NOT NULL DEFAULT 0;

ALTER TABLE products
ADD created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP;

ALTER TABLE products
MODIFY created_at DATETIME NOT NULL DEFAULT NOW();

INSERT INTO products(name, price) VALUES("iphone 13", 900);

DELETE FROM products;

SELECT * FROM products;

SELECT from_unixtime(unix_timestamp(created_at), '%Y-%m-%d') FROM products;

SELECT * FROM products
WHERE from_unixtime(unix_timestamp(created_at), '%Y-%m-%d') > '2022-11-30';

SELECT id, name, price, inventory, on_sale, from_unixtime(unix_timestamp(created_at), '%Y-%m-%d') FROM products;

SELECT * FROM products WHERE inventory < 300 AND price <= 500;

SELECT * FROM products WHERE name LIKE '%pro%';

SELECT * FROM products ORDER BY price DESC;

SELECT * FROM products WHERE price >= 300 ORDER BY price DESC LIMIT 5;