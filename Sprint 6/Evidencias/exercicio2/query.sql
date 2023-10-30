WITH Decades AS (
    SELECT
        "nome",
        "ano",
        "total",
        CASE
            WHEN "ano" BETWEEN 1950 AND 1959 THEN '1950s'
            WHEN "ano" BETWEEN 1960 AND 1969 THEN '1960s'
            WHEN "ano" BETWEEN 1970 AND 1979 THEN '1970s'
            WHEN "ano" BETWEEN 1980 AND 1989 THEN '1980s'
            WHEN "ano" BETWEEN 1990 AND 1999 THEN '1990s'
            WHEN "ano" BETWEEN 2000 AND 2009 THEN '2000s'
            WHEN "ano" BETWEEN 2010 AND 2019 THEN '2010s'
            WHEN "ano" BETWEEN 2020 AND 2029 THEN '2020s'
        END AS decade
    FROM "maintable"
)
, RankedNames AS (
    SELECT
        "nome",
        decade,
        "total",
        ROW_NUMBER() OVER (PARTITION BY decade ORDER BY "total" DESC) AS name_rank
    FROM Decades
)
SELECT
    "nome",
    decade,
    "total"
FROM RankedNames
WHERE name_rank <= 3
ORDER BY decade, name_rank;
