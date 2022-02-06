USE Lab4_songs;
LOAD DATA INFILE '/Users/mariavieira/Desktop/ece140a/Lab4/Uploads/Songs_data.csv'
INTO TABLE Songs_data
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;
