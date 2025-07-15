-- 7.First add
-- Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.

-- execute: cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
-- then: cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

INSERT INTO first_table (id, name)
VALUES (89, "Best School")