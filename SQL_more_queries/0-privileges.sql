-- 0.My privileges
-- Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

-- run: echo "CREATE USER 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
-- then: echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
-- execute: cat 0-privileges.sql | mysql -hlocalhost -uroot -p
-- then: cat 0-privileges.sql | mysql -hlocalhost -uroot -p

SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';