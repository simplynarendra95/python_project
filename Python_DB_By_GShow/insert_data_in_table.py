import mysql.connector

# def select_data():
#     sql = "select *from student"
#     cursor = con.cursor()
#     cursor.execute(sql)
#     data = cursor.fetchall()
#     print(data)

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port=3306,
        database="geekyshow",
    )
    if con.is_connected:
        print("Database Connection...")
        sql = "insert into student(sid, name, roll_no, fees) values(%s, %s, %s, %s)"
        records = [
            (4, 'Sumit kumar', '104', '5000'),
            (5, 'Jitu', '105', '4000'),
            (6, 'Monu', '106', '6000'),
        ]
        cursor = con.cursor()
        cursor.executemany(sql, records)
        con.commit()
except:
    con.rollback()
    print("Unable to connect")
finally:    
    print("Record Inserted Successfully...")    
    con.close()

    print("Connection Closed......")