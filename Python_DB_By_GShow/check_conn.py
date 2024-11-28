from dataclasses import dataclass
import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port=3306,
        # database=''
    )
    if con.is_connected():
        print("Connection established....")
        # sql = "create database testdb"
        # cur = con.cursor()
        # cur.execute(sql)
except:
    print("Unnable to connect....")

finally:
    sql = "show databases"
    cur = con.cursor()
    cur.execute(sql)
    for d in cur:
        print(d)
    con.close()
    print("Connection Closed....")