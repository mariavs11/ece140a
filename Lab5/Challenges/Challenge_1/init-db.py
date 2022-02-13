import mysql.connector as mysql
import os
import datetime
from dotenv import load_dotenv  # only required if using dotenv for creds

load_dotenv('credentials.env')
db_host = os.environ['MYSQL_HOST']
db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']

db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS Triton_Gallery;") # creates DB Triton Gallery
cursor.execute("USE Triton_Gallery")
cursor.execute("DROP TABLE IF EXISTS Gallery_Details;")

try:
    cursor.execute("""CREATE TABLE Gallery_Details (
      ID          integer  AUTO_INCREMENT PRIMARY KEY,
      Name        VARCHAR(50) NOT NULL,
      Owner       VARCHAR(50) NOT NULL,    
      Height  int,
      Age  int
    );
  """)
except RuntimeError as err:
    print("runtime error: {0}".format(err))

query = "INSERT INTO Gallery_Details (Name, Owner, Height, Age) VALUES (%s, %s, %s, %s)"
values = [
 ('Geisel-1.jpg','Terrell Gilmore',163, 45),
 ('Geisel-2.jpg','Sila Mann',189,51),
 ('Geisel-3.jpg','Nyle Hendrix',152, 27),
 ('Geisel-4.jpg','Axel Horton',176,21),
 ('Geisel-5.jpg','Courtney Mcneil',172,64)
]
cursor.executemany(query, values)
db.commit()

# BASIC SELECT
cursor.execute('SELECT * from Gallery_Details;')
my_result = cursor.fetchall()
print('---SELECT---')
[print(x) for x in my_result]

db.commit()