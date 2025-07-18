-- 1.Root user
-- Write a script that creates the MySQL server user user_0d_1.

-- execute: cat 1-create_user.sql | mysql -hlocalhost -uroot -p
-- then: cat 0-privileges.sql | mysql -hlocalhost -uroot -p

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';


-- https://www.datacamp.com/doc/mysql/mysql-grant