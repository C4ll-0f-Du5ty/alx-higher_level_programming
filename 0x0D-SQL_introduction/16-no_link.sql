-- List the data in specific way
SELECT score,
    name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
