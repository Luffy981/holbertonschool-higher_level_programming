-- ists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT ts.title FROM tv_shows AS ts
LEFT JOIN
(
	SELECT ts.id FROM tv_shows AS ts
	JOIN tv_show_genres AS tsg
	ON ts.id=tsg.show_id
	JOIN tv_genres AS tg
	ON tsg.genre_id=tg.id
	WHERE tg.name = "Comedy"
) AS subselect
ON subselect.id = ts.id WHERE subselect.id IS NULL ORDER BY ts.title ASC;
