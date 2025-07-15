-- 12.Cheating is bad
-- Write a script that updates the score of Bob to 10 in the table second_table.

-- execute: cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

UPDATE second_table
set score = 10
WHERE name = "Bob";


SELECT score, name FROM second_table
ORDER by score DESC;

-- https://www.w3schools.com/sql/sql_update.asp