import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="covid"
)

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")
# mycursor.execute("CREATE TABLE post (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), request VARCHAR(255), location VARCHAR(255), status BOOLEAN)")

for x in mycursor:
  print(x)