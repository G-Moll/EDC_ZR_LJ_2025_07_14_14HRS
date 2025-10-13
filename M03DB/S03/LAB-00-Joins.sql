USE digistore;
SHOW TABLES;
DESCRIBE Makers;
DESCRIBE Products;

-- Standard Query
SELECT fields
FROM Table
WHERE conditions
;


-- Join Query
SELECT fields
FROM Table  -- Makers   	id
JOIN Table  -- Products 	maker_id
ON id = maker_id;


SELECT * FROM Makers;
SELECT * FROM Products;
SELECT * FROM Products WHERE maker_id = 2;

SELECT Products.id, Products.name, price, Makers.id, Makers.name
FROM Makers    -- Makers   	id
JOIN Products  -- Products 	maker_id
ON Makers.id = Products.maker_id
;





