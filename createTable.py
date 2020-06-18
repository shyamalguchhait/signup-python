import mysql.connector

imDB=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="login"
)
db=imDB.cursor()
db.execute("CREATE TABLE login(id SERIAL PRIMARY KEY, name VARCHAR(255),username VARCHAR(255),email VARCHAR(255),phone_no INT(255), password VARCHAR(255))")
print("CREATE table successfully")