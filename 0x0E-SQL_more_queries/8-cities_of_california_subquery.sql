-- 
USE hbtn_0d_usa; -- connect to data base

-- Get the id of California from the states table
SELECT id FROM states WHERE name = 'California';

-- Use the id of California to select the cities
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id;

