import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="0113",
    database="daftarcheh"
)
mycursor=mydb.cursor()
#mycursor.execute("CREATE TABLE contact ( id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255), address VARCHAR(255))")
name=input("plase enter your name : ")
addres=input("plase enter your addres : ")
val=name,addres
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = (name, addres)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")