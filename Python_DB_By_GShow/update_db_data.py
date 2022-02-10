import mysql.connector

try:
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        port = 3306,
        database='geekyshow',
    )
    if con.is_connected():
        print("----------------------------------------------")
        print("Database connection establishing ......")
        print("----------------------------------------------")
        cursor = con.cursor()
        sql = "update student set fees=8000 where sid=6"
        cursor.execute(sql)
        con.commit()
        print("----------------------------------------------")
        print(cursor.rowcount, "Data Updated.")
        print("Commited Successfully..")
        print("Database connection Successfully....")
        print("----------------------------------------------")
except:
    con.rollback()
    print("----------------------------------------------")
    print("Database Connection Failed !!!!")
    print("----------------------------------------------")
finally:
    print("----------------------------------------------")
    cursor.close()
    con.close()
    print("Database Connection Closed..")
    print("----------------------------------------------")