--  lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT t.name AS genre, SUM(r.rate) AS rating_sum
FROM tv_genres t
JOIN tv_show_genres g ON t.id = g.genre_id
JOIN tv_show_ratings r ON tsg.show_id = r.show_id
GROUP BY t.name
ORDER BY rating_sum DESC;
