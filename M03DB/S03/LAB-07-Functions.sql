USE digistore;
SHOW TABLES;
DESCRIBE Makers;
DESCRIBE Products;

-- Aggregate Functions

-- Query 1
SELECT COUNT( * )
FROM Products;

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
SELECT
	Makers.name AS "Maker",
	MAX( Products.price ) AS "MAX",
	MIN( Products.price ) AS "MIN",
	AVG( Products.price ) AS "AVG",
	COUNT( Products.price ) AS "UNITS"
FROM Products
LEFT JOIN Makers
ON Products.maker_id = Makers.id
GROUP BY Makers.id
HAVING AVG( Products.price ) > 250
;



-- Samples

SELECT COUNT( * )
FROM Products
WHERE maker_id = 2;

where Maker.name = "Asus"


SELECT * FROM Makers;
SELECT * FROM Products;
SELECT * FROM Products WHERE maker_id = 2;




SELECT MAX( price )
FROM Products;

SELECT MIN( price )
FROM Products;





-- FROM Products
-- LEFT JOIN Makers
-- ON...

-- FROM Makers
-- RIGHT JOIN Products
-- ON...

-- FROM Products
-- RIGHT JOIN Makers
-- ON...

