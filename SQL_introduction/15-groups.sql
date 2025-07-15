-- 15.Number by score
-- Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.

-- execute: cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score;

-- https://www.w3schools.com/sql/sql_groupby.asp