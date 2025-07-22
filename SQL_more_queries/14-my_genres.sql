-- 14.My genres
-- Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.

-- cat 14-my_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows

SELECT tv_genres.name 
FROM tv_shows JOIN tv_show_genres on tv_shows.id = tv_show_genres.show_id JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = "DEXTER"
ORDER BY tv_genres.name ASC;
