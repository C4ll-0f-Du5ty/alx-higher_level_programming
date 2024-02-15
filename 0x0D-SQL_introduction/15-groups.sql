-- Counting the Presence
SELECT score,
    COUNT(*) AS "number"
FROM second_table
GROUP BY score;
