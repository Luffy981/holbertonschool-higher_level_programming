-- script that lists all Comedy shows in the database hbtn_0d_tvshowsl
SELECT ts.title FROM tv_shows  AS ts JOIN tv_show_genres AS tn ON ts.id=tn.show_id JOIN tv_genres AS tg ON tn.genre_id=tg.id WHERE tg.name="Comedy" ORDER BY ts.title ASC;
