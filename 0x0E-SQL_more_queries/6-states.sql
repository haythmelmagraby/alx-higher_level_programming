-- creates the database hbtn_0d_usa and the table states
CREATE DATABSE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREAMENT PRIMARY KEY, name VARCHAR(256) NOT NULL);
