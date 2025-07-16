-- 5.Unique ID
-- Write a script that creates the table unique_id on your MySQL server.

/*
execute: cat 5-unique_id.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
echo 'INSERT INTO unique_id (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
echo 'SELECT * FROM unique_id;' | mysql -hlocalhost -uroot -p hbtn_0d_2
echo 'INSERT INTO unique_id (id, name) VALUES (89, "Best");' | mysql -hlocalhost -uroot -p hbtn_0d_2
echo 'SELECT * FROM unique_id;' | mysql -hlocalhost -uroot -p hbtn_0d_2
*/

CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);


-- https://www.w3schools.com/sql/sql_unique.asp