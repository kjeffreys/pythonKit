from config import *
import mysql.connector

config = {
    'user': USER,
    'password': PW,
    'host': HOST,
    'database': DB,
    'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cnx.close()
