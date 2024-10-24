CREATE DATABASE IF NOT EXISTS sample_db;

USE sample_db;

CREATE TABLE IF NOT EXISTS sample_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

INSERT INTO sample_table (name) VALUES ('Sample Data 1'), ('Sample Data 2');

