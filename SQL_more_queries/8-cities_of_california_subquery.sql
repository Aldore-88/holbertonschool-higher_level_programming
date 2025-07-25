-- 8.Cities of California
-- Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.

-- echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
-- echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
-- cat 8-cities_of_california_subquery.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa

SELECT id, name FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = "California"
);
