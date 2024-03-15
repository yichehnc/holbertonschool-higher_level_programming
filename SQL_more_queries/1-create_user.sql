-- Creates a new user in the MySQL database
CREATE USER IF NOT EXISTS 'user_0d_1'@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@localhost;