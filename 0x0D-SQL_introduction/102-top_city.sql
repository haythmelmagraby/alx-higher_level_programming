-- that displays the top 3 of cities temperature 
SELECT city, AVG(value) AS avg_temp from temperatures where month in (7, 8) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
