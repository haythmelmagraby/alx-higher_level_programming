-- lists all records of the table second_table with names
SELECT score, name FROM second_table HAVING NAME IS NOT NULL ORDER BY score DESC;
