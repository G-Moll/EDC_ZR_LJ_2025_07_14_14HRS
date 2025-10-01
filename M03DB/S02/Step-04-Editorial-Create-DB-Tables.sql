-- 3) Modelo Físico
CREATE DATABASE Editorial;
USE Editorial;

CREATE TABLE Branches(
    id INT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
    code VARCHAR( 10 ) NOT NULL,
    address VARCHAR( 120 ) NOT NULL,
    phone VARCHAR( 15 )
);

CREATE TABLE Employees(
    id INT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
    rfc VARCHAR( 22 ) NOT NULL,
    name VARCHAR( 50 ) NOT NULL,
    lastname VARCHAR( 80 ) NOT NULL,
    birthday DATE NOT NULL,
    entrydate DATE NOT NULL,
    phone VARCHAR( 15 ),

    branch_id INT UNSIGNED NOT NULL,
    FOREIGN KEY( branch_id ) REFERENCES Branches( id )
);

DESCRIBE Branches;
DESCRIBE Employees;
