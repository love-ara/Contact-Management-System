import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
<<<<<<< HEAD
    password="imotua26"
=======
    password="Password"
>>>>>>> origin/update
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE contact_management_system")

print("Database created successfully")
