-- 3.Always a name
-- Write a script that creates the table force_name on your MySQL server.

-- execute: cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
-- echo 'INSERT INTO force_name (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
-- echo 'SELECT * FROM force_name;' | mysql -hlocalhost -uroot -p hbtn_0d_2
-- echo 'INSERT INTO force_name (id) VALUES (333);' | mysql -hlocalhost -uroot -p hbtn_0d_2
-- echo 'SELECT * FROM force_name;' | mysql -hlocalhost -uroot -p hbtn_0d_2

CREATE TABLE IF NOT EXISTS force_name(
    id INT,
    name VARCHAR(256)
);
