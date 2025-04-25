import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="0113"
)
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE daftarcheh")

