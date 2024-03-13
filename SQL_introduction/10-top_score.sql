-- Lists all records of the table in the databases with records ordered by top score
SELECT score, name
FROM second_table
ORDER BY score DESC