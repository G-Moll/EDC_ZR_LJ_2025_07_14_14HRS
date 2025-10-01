USE Editorial;

-- id (PK) RFC     name         lastname    birthday    entrydate   phone           branch_id (FK)
-- 1   JORO7581AZ  Joshua       Rodríguez   2011-05-10  2022-11-06  55 7175 4350    1
-- 2   AUFE4529AZ  Aurora       Fernández   1998-02-03  2018-05-13  56 6340 7207    3
-- 3   JUFE5395NZ  Juan         Fernández   2000-01-23  2005-09-21  55 6429 3880    2
-- 4   ALPE6098OZ  Alberto      Pérez       2008-10-02  1996-03-26  56 2520 8284    1
-- 5   RAPE8157LZ  Raquel       Pérez       1996-07-12  2000-12-10  56 6703 6629    4
-- 6   NALO5337YZ  Nataly       López       2000-09-11  1999-01-25  55 8520 1983    2
-- 7   ALHE6325OZ  Alejandro    Hernández   2005-03-20  1991-07-14  56 3627 6284    3
-- 8   ROPE2654OZ  Rodrigo      Peláez      2001-04-14  2003-03-03  56 6608 9170    3


INSERT INTO Employees VALUES
    ( NULL, "JORO7581AZ", "Joshua",    "Rodríguez", "2009-12-11",  "2021-06-15", "55 7175 4350", 1 ),
    ( NULL, "AUFE4529AZ", "Aurora",    "Fernández", "1990-05-11",  "2022-04-03", "56 6340 7207", 3 ),
    ( NULL, "JUFE5395NZ", "Juan",      "Fernández", "2013-04-03",  "2020-11-20", "55 6429 3880", 2 ),
    ( NULL, "ALPE6098OZ", "Alberto",   "Pérez",     "1996-09-01",  "2023-10-28", "56 2520 8284", 1 ),
    ( NULL, "RAPE8157LZ", "Raquel",    "Pérez",     "1992-06-21",  "2021-04-20", "56 6703 6629", 4 ),
    ( NULL, "NALO5337YZ", "Nataly",    "López",     "2013-03-01",  "2020-05-19", "55 8520 1983", 2 ),
    ( NULL, "ALHE6325OZ", "Alejandro", "Hernández", "2017-11-14",  "2022-12-23", "56 3627 6284", 3 ),
    ( NULL, "ROPE2654OZ", "Rodrigo",   "Peláez",    "2000-03-18",  "2022-11-12", "56 6608 9170", 3 )
;

-- ERROR, Branch 10 Doesn't exist...
INSERT INTO Employees VALUES( NULL, "PERO7581AZ", "Peter", "Rodríguez", "2011-05-10",  "2022-11-06" , "55 7175 4350", 10 );
-- OK
INSERT INTO Employees VALUES( NULL, "PERO7581AZ", "Peter", "Rodríguez", "2011-05-10",  "2022-11-06" , "55 7175 4350", 1 );

DESCRIBE Employees;

SELECT * FROM Employees;
