# here we delete the data from Table Parameterized Oqery in Python.

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
    print("*********************************")
    print("Establish Database Connection...")
    time.sleep(5)
    if con.is_connected():
        print("Database Connected Successfully")
        print("******************************")
        time.sleep(4)
        cursor = con.cursor()
        
        # 1.0.0
        # sql = "delete from student where sid=%s"
        # del_value=(8,)
        # cursor.execute(sql, del_value)

        # 1.0.1
        # here we use input() for taking a input from enduser and then delete 
        # the data from database in python.
        # sql = "delete from student where sid=%s"
        # data = input("Enter the student id here ::")
        # del_value=(data,)
        # cursor.execute(sql, del_value)
        
        # 1.0.2
        sql = "delete from student where sid=%(sid)s"
        if sql:
            cursor.execute(sql, {'sid': 8})
            con.commit()
            # print(cursor.rowcount, 'Row Delete')
        else:
            print("Not delete the data...")

        # 1.0.0
        select_sql = "select *from student"
        cursor.execute(select_sql)
        data = cursor.fetchall()
        # print(data)
        for row in data:
            print("Student ID: {} Name: {} Roll-No: {} Fees: {}".format(row[0], row[1], row[2], row[3]))
        time.sleep(4)        
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