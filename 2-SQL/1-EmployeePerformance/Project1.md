
- Allow local file to be loaded https://stackoverflow.com/questions/66848547/mysql-error-code-3948-loading-local-data-is-disabled-this-must-be-enabled-on-b

- ALSO ADD TO MYSQL CONNECTON SETTINGS: ADVANCED > OTHERS > OPT_LOCAL_INFILE=1


1.  How to import csv into db - https://www.geeksforgeeks.org/how-to-import-timestamp-from-a-csv-file-in-mysql/

-- 1. create table
CREATE TABLE table_name(
id INTEGER,
col_1 VARCHAR(100),
col_2 INTEGER,
col_3 DATETIME DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (id)
);
-- 2. load data into table
LOAD DATA INFILE '{folder_structure}/{csv_file_name}'
INTO TABLE table_name
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


LOAD DATA LOCAL INFILE 'yourfile.csv'
INTO TABLE yourTable
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n' 
(@Date, HomeTeam, AwayTeam, FTHG, FTAG, FTR, HTHG, HTAG, HTR)
SET Date = STR_TO_DATE(@Date, '%d/%m/%Y');

https://stackoverflow.com/questions/76133326/mysql-how-to-upload-csv-dates-from-mm-dd-yyyy-directly-into-a-date-data-type-f

LOAD DATA LOCAL INFILE 'C:/Users/LK/Desktop/Date Import Test.csv'
INTO TABLE Test_Table
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(@date_col, blah_col1, blah_col2)
SET date_col = STR_TO_DATE(@date_col, '%m/%d/%Y');


https://medium.com/@tushar0618/how-to-create-er-diagram-of-a-database-in-mysql-workbench-209fbf63fd03


