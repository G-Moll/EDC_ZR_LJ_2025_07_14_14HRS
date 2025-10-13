USE digistore;
SHOW TABLES;
DESCRIBE Makers;
DESCRIBE Products;

-- Query 1
SELECT name
FROM Products;

-- Query 2
SELECT name, price
FROM Products;

-- Query 3
SELECT *
FROM Products;


-- Query 4
SELECT *
FROM Products
WHERE maker_id = (
	SELECT id
	FROM Makers
	WHERE name = "Lenovo"
);


-- Query 5
SELECT * FROM Makers;
SELECT * FROM Products;

SELECT *
FROM Products
WHERE price = (
	SELECT MAX( price )
	FROM Products
	WHERE maker_id = (
		SELECT id
		FROM Makers
		WHERE name = "Lenovo"
		)
);


-- Query 6





-- Samples
SELECT * FROM Products;

SELECT *
FROM Products
WHERE maker_id = 6 OR price >= 200
-- WHERE maker_id = 6 AND price >= 200
;

