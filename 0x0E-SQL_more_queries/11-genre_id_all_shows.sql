-- script that lists all shows contained in the database hbtn_0d_tvshows
SELECT tvs.title, tvsg.genre_id FROM tv_shows AS tvs LEFT JOIN tv_show_genres AS tvsg ON tvs.id=tvsg.show_id ORDER BY tvs.title, tvsg.genre_id ASC;
