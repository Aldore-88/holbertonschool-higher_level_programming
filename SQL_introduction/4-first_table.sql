-- 4.First Table
-- first: cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
-- execute: cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
-- then: cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

CREATE TABLE if NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
