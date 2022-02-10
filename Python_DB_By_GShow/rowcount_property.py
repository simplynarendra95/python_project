# here we check the number of inserted rows in database.

import mysql.connector

try:    
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port=3306,
        database="geekyshow",
    )

    if con.is_connected():
        print("Database connected successfully....")
        cursor = con.cursor()
        sql ="insert into student(sid, name, roll_no, fees) values(7, 'Ankit', 107, 8000)"
        cursor.execute(sql)
        con.commit()
        print(cursor.rowcount, "Row Inserted Successfully....")
except:
    con.rollback()
    print("Connection Unsuccessfully .....")
finally:
    cursor.close()
    con.close()