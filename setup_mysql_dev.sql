-- MySQL server for AirBNBClone2

IF NOT EXISTS CREATE DATABASE hbnb_dev_db;
IF NOT EXISTS CREATE USER hbnb_dev indetified by hbnb_dev_pwd;
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema TO 'hbnb_dev'@'localhost';
