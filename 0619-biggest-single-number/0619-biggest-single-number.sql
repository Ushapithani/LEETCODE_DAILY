SELECT MAX(num) AS num
FROM (
    SELECT DISTINCT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
) AS t;