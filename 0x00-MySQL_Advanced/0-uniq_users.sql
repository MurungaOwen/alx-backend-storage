-- script to create a table for users
-- create users table with id email and name
CREATE TABLE IF NOT EXISTS users(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,email VARCHAR(255) NOTNULL, name VARCHAR(255));