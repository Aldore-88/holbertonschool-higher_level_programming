-- 6.States table
-- Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.


-- cat 6-states.sql | mysql -hlocalhost -uroot -p
-- echo 'INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
-- echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
    id INT UNIQUE AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
)

-- https://www.w3schools.com/sql/sql_primarykey.ASP
-- https://www.w3schools.com/sql/sql_autoincrement.asp
