-- Lists all records of the table in the databases with records ordered by top score and score >= 10
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC