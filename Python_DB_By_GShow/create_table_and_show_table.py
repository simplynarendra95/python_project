import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        # port=3306,
        database="geekyshow",
    )
    if con.is_connected:
        print("Database Connection Establish Successfully ....")
        sql = "create table student(sid integer(20) primary key, name varchar(255), roll_no integer(10), fees integer(50))"
        cursor = con.cursor()
        cursor.execute(sql)  

except:
    print("Database Connection Not Successfully ....")

finally:
    # sql = "create table student(sid int auto_increment primary key, name varchar(255), roll int(25), fees float()) "
    # cursor = con.cursor()
    # cursor.execute("create table student(sid integer(20) primary key, name varchar(255), roll_no integer(10), fees integer(50))")  
    
    # cursor.close()
    con.close()
    print("Connection Closed Successfully....")