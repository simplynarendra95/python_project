# here we delete the data from Table without Parameterized form.

# from os import curdir
# from sqlite3 import Cursor
import mysql.connector

try:
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        port=3306,
        database='geekyshow',
    )

    if con.is_connected():
        print("Database Connecting.....")
        cursor = con.cursor()
        sql = "delete from student where sid=7"
        cursor.execute(sql)
        con.commit()
        print("Data deletion Successfully....")
        print(cursor.rowcount, 'Row deleted.')
except:
    con.rollback()
    print("Database connection not successfully...")
finally:
    cursor.close()
    con.close()
    print("Database connection closed...")