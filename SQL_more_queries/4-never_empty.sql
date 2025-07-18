-- 4.ID cant be null
-- Write a script that creates the table id_not_null on your MySQL server.

/*
execute: cat 4-never_empty.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
echo 'INSERT INTO id_not_null (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
echo 'SELECT * FROM id_not_null;' | mysql -hlocalhost -uroot -p hbtn_0d_2
echo 'INSERT INTO id_not_null (name) VALUES ("Best");' | mysql -hlocalhost -uroot -p hbtn_0d_2
echo 'SELECT * FROM id_not_null;' | mysql -hlocalhost -uroot -p hbtn_0d_2
*/

CREATE TABLE IF NOT EXISTS id_not_null(
    id INT DEFAULT 1,
    name VARCHAR(256)
);

-- https://www.w3schools.com/sql/sql_default.asp