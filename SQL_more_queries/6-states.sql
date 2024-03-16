-- Creates the database hbtn_0d_usa and the table
-- states (in the database hbtn_0d_usa) in your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
DROP TABLE IF EXISTS hbtn_0d_usa.states;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);