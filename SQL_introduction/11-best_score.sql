-- Lists all records of the table in the databases with records ordered by top score and score >= 10
SELECT score, name
FROM second_table
WHERE socre >= 10
ORDER BY score DESC