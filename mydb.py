import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "imotua26"
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE contact_management_system")

print("Database created successfully")