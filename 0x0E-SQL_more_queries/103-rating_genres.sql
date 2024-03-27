--  lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT t.name, SUM(r.rate) AS rate_sum FROM tv_genres AS t
JOIN tv_show_genres as s on s.genre_id = t.id
JOIN tv_show_ratings AS r ON s.show_id = r.show_id
GROUP BY t.name ORDER BY rating DESC;
