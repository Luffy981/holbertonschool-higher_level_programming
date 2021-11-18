-- lists all cities contained in the database hbtn_0d_usa
SELECT c.id, c.name, s.name FROM cities AS c INNER JOIN states AS s WHERE s.state_id = c.id ORDER BY c.id ASC;
