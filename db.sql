CREATE DATABASE pubs_db;
use pubs_db;
CREATE TABLE pub (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(120) NOT NULL,
address VARCHAR(300),
year_opened INT,
budget FLOAT,
serve_food BOOLEAN DEFAULT FALSE,
google_review FLOAT,
live_music BOOLEAN DEFAULT FALSE
);