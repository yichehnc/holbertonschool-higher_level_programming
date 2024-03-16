-- Creates the table unique_id on the MySQL server
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256) NOT NULL
)