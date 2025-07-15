-- 8.Count 89
-- Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.

-- execute: cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1

USE hbtn_0c_0;
SELECT COUNT(*) 
FROM first_table
WHERE id = 89;

-- https://www.w3schools.com/sql/sql_count.asp