-- lists all bands with Glam rock as their main style
SELECT 
    band_name,
    TIMESTAMPDIFF(YEAR, formed, IFNULL(split, '2022-01-01')) AS lifespan
FROM 
    bands
WHERE 
    style = 'Glam rock'
ORDER BY 
    lifespan DESC;
