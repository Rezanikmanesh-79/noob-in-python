import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="0113",
    database="daftarcheh"
)
mycursor=mydb.cursor()
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
