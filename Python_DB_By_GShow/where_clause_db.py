# here we use fetchone() method for access only one result, 
# if we want more than one data by using fetchone() then we use while loop 
# and inside while loop we use fetchone() method.


import mysql.connector
import time


try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port=3306,
        database="geekyshow",
    )
    print("********************************")
    print("Establish a database connection with mysql database....")
    print("*********************************")
    time.sleep(5)
    if con.is_connected():
        print("Database connected")
        time.sleep(3)
        cursor = con.cursor()
        sql = "select *from student where fees = 5000"
        cursor.execute(sql)
        data = cursor.fetchone()
        while data is not None:
            print(data)
            data = cursor.fetchone()
        print(cursor.rowcount)

except mysql.connector.DatabaseError as e:
    time.sleep(3)
    con.rollback()
    print("database is not connected ::", e)
finally:
    time.sleep(5)
    cursor.close()
    con.close()
    print("*********************************")
    print("Database connection closed.")