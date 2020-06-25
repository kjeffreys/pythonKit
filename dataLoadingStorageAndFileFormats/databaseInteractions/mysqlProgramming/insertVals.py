from __future__ import print_function
from config import *
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta

if __name__ == "__main__":
    cnx = mysql.connector.connect(user=USER, password=PW, database='employees')
    cursor = cnx.cursor()

    tomorrow = datetime.now().date() + timedelta(days=1)

    addEmployee = ("INSERT INTO employees "
               "(first_name, last_name, hire_date, gender, birth_date) "
               "VALUES (%s, %s, %s, %s, %s)")

    addSalary = ("INSERT INTO salaries "
              "(emp_no, salary, from_date, to_date) "
              "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")

    dataEmployee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))

    # Insert new employee
    cursor.execute(addEmployee, dataEmployee)
    empNo = cursor.lastrowid

    # Insert salary information
    dataSalary = {
        'emp_no': empNo,
        'salary': 50000,
        'from_date': tomorrow,
        'to_date': date(9999, 1, 1),
    }

    cursor.execute(addSalary, dataSalary)

    # Make sure data is committed to the db
    cnx.commit()

    cursor.close()
    cnx.close()

