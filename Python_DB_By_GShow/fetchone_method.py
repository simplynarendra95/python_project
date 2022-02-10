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
    print("----------------------------------------------")
    print("Database connection establishing ......")
    # print("----------------------------------------------")
    time.sleep(5)
    if con.is_connected():
        print("----------------------------------------------")
        print("Database Connected .")
        time.sleep(5)
        print("----------------------------------------------")
        cursor = con.cursor()
        sql = "select *from student"
        cursor.execute(sql)
        row = cursor.fetchone()
        while row is not None:
            # print(row)
            sid = row[0]
            name = row[1]
            roll_no = row[2]
            fees = row[3]
            print("Student ID: {} Name: {} Roll-No: {} Fees: {}".format(sid, name, roll_no, fees))
            row = cursor.fetchone()
        con.commit()
        print("----------------------------------------------")
        time.sleep(3)
        print("Number Of Rows ::", cursor.rowcount)
        print("Commited Successfully..")
        time.sleep(2)
        print("Database connection Successfully....")
        print("----------------------------------------------")
    
except mysql.connector.DatabaseError as e:
    if con:
        con.rollback()
        print("----------------------------------------------")
        print("Database Connection Failed !!!!")
        print("There is problem with sql.")
        print("----------------------------------------------")
    
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    time.sleep(3)
    print("Database Connection Closed..")
    print("----------------------------------------------")