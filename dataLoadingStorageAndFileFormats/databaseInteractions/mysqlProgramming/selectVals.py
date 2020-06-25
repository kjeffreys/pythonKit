from __future__ import print_function
import datetime
import mysql.connector
from config import *




if __name__ == "__main__":
    cnx = mysql.connector.connect(user=USER, password=PW, database='employees')
    cursor = cnx.cursor()

    query = ("SELECT first_name, last_name, hire_date FROM employees "
         "WHERE hire_date BETWEEN %s AND %s")

    hire_start = datetime.date(2019, 1, 1)
    hire_end = datetime.date(2022, 12, 31)
    print(hire_start)
    print(hire_end)

    cursor.execute(query, (hire_start, hire_end))

    for (first_name, last_name, hire_date) in cursor:
        print("{}, {} was hired on {:%d %b %Y}".format(
        last_name, first_name, hire_date))
        print("!")
    cursor.close()
    cnx.close()