import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  database= "planner",
  user="root",
  password="mysql"
)

mycursor = db.cursor()