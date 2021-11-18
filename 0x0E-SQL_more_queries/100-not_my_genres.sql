-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT tg.name FROM tv_genres AS tg
LEFT JOIN
(
	SELECT tg.id FROM tv_genres AS tg
	JOIN tv_show_genres AS tsg
   		ON tg.id=tsg.genre_id
	JOIN tv_shows AS ts 
		ON tg.show_id=ts.id
	WHERE ts.title="Dexter"
	ORDER BY tg.name ASC
) AS subselect
ON subselect.id=tg.id WHERE subselect.id IS NULL ORDER BY tg.name ASC;
