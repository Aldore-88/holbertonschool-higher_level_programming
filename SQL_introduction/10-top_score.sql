-- 10.List by best
-- Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

-- execute: cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

SELECT score, name FROM second_table
ORDER by score DESC;

-- https://www.w3schools.com/sql/sql_orderby.asp
-- https://www.w3schools.com/sql/sql_select.asp