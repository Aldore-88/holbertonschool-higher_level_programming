-- 7. Cities table
-- Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.

-- cat 7-cities.sql | mysql -hlocalhost -uroot -p
-- echo 'INSERT INTO cities (state_id, name) VALUES (1, "San Francisco");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
-- echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
-- echo 'INSERT INTO cities (state_id, name) VALUES (10, "Paris");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
-- echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities
(
    id INT UNIQUE AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256),
    FOREIGN KEY(state_id) REFERENCES states(id)
)

-- ???PRIMARY VS FOREIGN KEY!!!

-- https://www.w3schools.com/sql/sql_foreignkey.asp
