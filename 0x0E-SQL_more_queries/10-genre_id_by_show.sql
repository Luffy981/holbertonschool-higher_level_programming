-- Import the database dump from hbtn_0d_tvshows
SELECT tvs.title, tvsg.genre_id FROM tv_shows AS tvs JOIN tv_show_genres AS tvsg WHERE tvs.id=tvsg.show_id ORDER BY tvs.title, tvsg.genre_id ASC;
