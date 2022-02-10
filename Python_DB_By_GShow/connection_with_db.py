import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port=3306,
        database="geekyshow",
    )
    if con.is_connected:
        print("Database Connection Successfully ......")

except:
    print("Unable to connect....")

finally:
    con.close()
    print("Database connection closed...")