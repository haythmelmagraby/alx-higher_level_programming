--  lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT name, SUM(rate) AS rating FROM tv_genres AS t
INNER JOIN tv_show_genres as s on s.genre_id = t.id
INNER JOIN tv_show_ratings AS r ON s.show_id = r.show_id
GROUP BY name ORDER BY rating DESC;
