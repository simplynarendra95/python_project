# from typing import final

# here we update the data from Table Parameterized Oqery in Python.

from turtle import update
import mysql.connector
import time

try:
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password = 'root',
        port=3306,
        database='geekyshow',
    )
    print("*********************************")
    print("Establish Database Connection...")
    time.sleep(5)
    if con.is_connected():
        print("Database Connected Successfully")
        print("******************************")
        cursor = con.cursor()
    # 1.0.0 update query.
        # sql = "update student set fees=5500 where sid=4 "
        # data = cursor.execute(sql)
        # print(cursor.rowcount, "Update Data in DB.")

    # 1.0.1
    # here we use parameterized query('%s', '%s') for update the data in existing db table.
        sql = "update student set roll_no=%s where sid=%s"
        # here we pass data as tuple format only.
        # cursor.execute(sql, (109, 9))
        # print(cursor.rowcount, "Update Data in DB.")
    
    # 1.0.1
        # sql = "update student set roll_no=%s where sid =%s"
        # update_val = (107, 7)
        # cursor.execute(sql, update_val)
        # print(cursor.rowcount, "Update Data in DB.")
    
    # 1.0.2
        sql = "update student set name=%s where sid=%s"
        update_val = ('John', 7)
        cursor.execute(sql, update_val)
        print(cursor.rowcount, "Update Data in DB.")

        
        con.commit()
except mysql.connector.DatabaseError as e:
    time.sleep(3)
    con.rollback()
    print("Unable to delete the data")    
finally:
    time.sleep(3)
    if cursor:
        cursor.close()
    if con:
        con.close()
    print("Connection is closed....")