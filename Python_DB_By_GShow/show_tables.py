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
        print("Database connection .....")
        sql = "show tables"
        cur = con.cursor()
        cur.execute(sql)
        for t in cur:
            print(t)
except:
    pass

finally:
    if cur:
        cur.close()
    if con:
        con.close()
    