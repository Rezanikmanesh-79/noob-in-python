import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="0113"
)
dalal = mydb.cursor()
dalal.execute("CREATE DATABASE daneshgah")
print(mydb)