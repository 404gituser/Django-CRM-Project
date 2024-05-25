import mysql.connector

databaseObj = mysql.connector.connect(
    host= 'localhost',
    passwd= "admin123",
    user= "root"
)

print(databaseObj)

cursorOobj = databaseObj.cursor()

# cursorOobj.execute("CREATE DATABASE CRM")

print("ALL DONE")