import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="covid"
)

mycursor = mydb.cursor()

def create(username, request, location):
    sql = "INSERT INTO post (username, request, location) VALUES (%s, %s, %s)"
    val = (username, request, location)
    mycursor.execute(sql, val)

    mydb.commit()

def update(username, request, location):
    sql = "INSERT INTO post (username, request, location) VALUES (%s, %s, %s)"
    val = (username, request, location)
    mycursor.execute(sql, val)

    mydb.commit()