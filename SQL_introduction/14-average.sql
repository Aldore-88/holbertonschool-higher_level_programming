-- 14.Average
-- Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.

-- excute: cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

SELECT AVG(score) AS average FROM second_table;

-- https://www.w3schools.com/sql/sql_aggregate_functions.asp
-- https://www.w3schools.com/sql/sql_avg.asp

