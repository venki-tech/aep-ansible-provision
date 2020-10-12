#!/usr/bin/env python3

import mysql.connector as mysql

HOST = "3.10.179.9"
PORT = 3306
USER = "root"
PASSWORD = "Passw0rd!23"
DB = "db_emp_db"

try:
    connection = mysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB)

    dbhandler = connection.cursor()
    dbhandler.execute("SELECT * from tbl_emp_db")
    result = dbhandler.fetchall()
    for item in result:
        print (item)

except Exception as e:
    print (e)

finally:
    connection.close()

