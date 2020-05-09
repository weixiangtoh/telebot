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
  return mycursor.lastrowid


def search(username):
  sql = "SELECT * FROM post where username = %s"
  val = (username,)
  mycursor = mydb.cursor()
  mycursor.execute(sql, val)
  myresult = mycursor.fetchall()
  return myresult

def getPost(id):
  sql = "SELECT * FROM post where id = %s"
  val = (id,)
  mycursor = mydb.cursor()
  mycursor.execute(sql, val)
  myresult = ''
  myresult = mycursor.fetchall()
  return myresult

def delete(id):
  sql = "DELETE FROM post WHERE id = %s"
  val = (id, )
  mycursor.execute(sql, val)
  mydb.commit()


# def update(status):
#     sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
#     val = (username, request, location)
#     mycursor.execute(sql, val)
#     mydb.commit()