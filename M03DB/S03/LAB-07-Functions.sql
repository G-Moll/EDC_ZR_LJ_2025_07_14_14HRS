USE digistore;
SHOW TABLES;
DESCRIBE Makers;
DESCRIBE Products;

-- Aggregate Functions

-- Query 1
SELECT COUNT( * )
FROM Products;

-- SELECT COUNT( * )
-- FROM Products
-- WHERE maker_id = 2;

-- Query 2
SELECT
	Makers.name,
	COUNT( Products.id )
FROM Makers
JOIN Products
ON Products.maker_id = Makers.id
GROUP BY Makers.id
ORDER BY 2 DESC
;


-- Query 3
SELECT
	Makers.name,
	MAX( Products.price ),
	MIN( Products.price ),
	AVG( Products.price ),
	COUNT( Products.price )
FROM Makers
JOIN Products
ON Products.maker_id = Makers.id
GROUP BY Makers.id
;



-- Query 4




SELECT * FROM Makers;
SELECT * FROM Products;
SELECT * FROM Products WHERE maker_id = 2;



-- Samples
SELECT MAX( price )
FROM Products;

SELECT MIN( price )
FROM Products;
