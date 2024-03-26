-- displays the max temperature 
SELECT state, MAX(vlaue) AS max_temp FROM remperatures GROUP BY state ORDER BY state;
