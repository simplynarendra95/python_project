# here insert a student data from keyboard.

# from click import option
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
        print("Database Connected Successfully....")
        print("*********************************")
        time.sleep(4)
        cursor = con.cursor()
        while True:
            sid = input("Enter Student Id ::")
            name = input("Enter Student Name ::")
            roll_no = input("Enter Student Roll Number ::")
            fees = input("Enter Student Fees ::")
            sql = "insert into student values(%s, %s, %s, %s)"
            # cursor = con.execute(sql %(sid, name, roll_no, fees))
            # cursor = con.execute(sql)
            cursor.execute(sql, (sid, name, roll_no, fees))
            print("Record Inserted Successfully !!!")
            option=input("Do you want to insert one more record [Y | N]:")
            if option == "N" or "n":
                con.commit()
                break

except mysql.connector.DatabaseError as e:
    if con:
        con.rollback()
        print("There is problem with sql ::", e)
        
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print("DataBase connection is closed...")
    