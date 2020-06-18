import mysql.connector

cDB=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
db=cDB.cursor()
db.execute("CREATE DATABASE login")
print("CREATE database successfully")