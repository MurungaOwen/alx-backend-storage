-- rank country by fans
-- field returned are origin and total fans
SELECT origin, SUM(fans) AS nb_fans FROM metal_bands
GROUP BY (origin)
ORDER BY SUM(fans) DESC;