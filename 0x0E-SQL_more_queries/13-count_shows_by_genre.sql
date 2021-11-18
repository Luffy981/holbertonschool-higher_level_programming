-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT g.name AS genre, COUNT(tg.genre_id) AS number_of_shows FROM tv_genres AS g JOIN tv_show_genres AS tg ON g.id=tg.genre_id GROUP BY tg.genre_id ORDER BY number_of_shows DESC;
