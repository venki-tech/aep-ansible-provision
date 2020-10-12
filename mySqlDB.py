#!/usr/bin/env python3

import mysql.connector as mysql

HOST = "3.11.9.133"
PORT = 3306
USER = "root"
PASSWORD = "Passw0rd!23"
DB = "db_emp_db"

try:
    connection = mysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB)
    print ("Content-type: text/html\n\n")
    print ("<html>\n<body>")
    print ("<div style=\"width: 100%; font-size: 40px; font-weight: bold; text-align: center;\">")
    print ("AEP Test DB")
    print ("</div>\n")

    dbhandler = connection.cursor()
    dbhandler.execute("SELECT * from tbl_emp_db")
    result = dbhandler.fetchall()
    for item in result:
        print ("\n")
        print (item)
        print ("\n")
    print ("\n\n\n")
    print ("</body>\n</html>")

except Exception as e:
    print (e)

finally:
    connection.close()
