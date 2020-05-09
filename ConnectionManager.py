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


def search(username):
    sql = "SELECT * FROM post where username = %s"
    val = (username,)
    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult


# def update(id):
#     sql = "INSERT INTO post (username, request, location) VALUES (%s, %s, %s)"
#     val = (username, request, location)
#     mycursor.execute(sql, val)
#     mydb.commit()