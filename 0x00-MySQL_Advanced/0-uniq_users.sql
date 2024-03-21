-- script to create a table users
-- create table users with attribute id email name
CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, email VARCHAR(255) NOT NULL UNIQUE, name VARCHAR(255));