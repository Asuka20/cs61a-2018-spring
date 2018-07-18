.read lab12.sql

-- Q5
CREATE TABLE greatstudents AS
  SELECT s0.date, s0.color, s0.pet, s0.number, s1.number
  FROM students AS s0, fa17students AS s1
  WHERE s0.date = s1.date AND s0.color = s1.color AND s0.pet = s1.pet;

-- Q6
CREATE TABLE sevens AS
  SELECT s.seven 
  FROM students AS s, checkboxes AS c
  WHERE s.time = c.time AND s.number = 7 AND c.'7' = 'True';

-- Q7
CREATE TABLE fa17favnum AS
  SELECT number, COUNT(*) AS count  
  FROM fa17students 
  GROUP BY number 
  ORDER BY count DESC 
  LIMIT 1;


CREATE TABLE fa17favpets AS
  SELECT pet, COUNT(*) AS count  
  FROM fa17students 
  GROUP BY pet 
  ORDER BY count DESC 
  LIMIT 10;

CREATE TABLE sp18favpets AS
  SELECT pet, COUNT(*) AS count  
  FROM students 
  GROUP BY pet 
  ORDER BY count DESC 
  LIMIT 10;


CREATE TABLE sp18dog AS
  SELECT pet, COUNT(*) AS count  
  FROM students 
  WHERE pet = "dog";


CREATE TABLE sp18alldogs AS
  SELECT pet, COUNT(*) AS count  
  FROM students 
  WHERE pet LIKE "%dog%";


CREATE TABLE obedienceimages AS
  SELECT seven, denero, COUNT(*)
  FROM students 
  WHERE seven = '7' 
  GROUP BY denero;

-- Q8
CREATE TABLE smallest_int_count AS
  SELECT smallest, COUNT(*) AS count
  FROM students 
  GROUP BY smallest
  ORDER BY smallest;
