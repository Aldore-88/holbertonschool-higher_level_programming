-- 9.Cities by States

-- echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
-- echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
-- cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id=states.id;

-- https://www.w3schools.com/sql/sql_join.asp
