from config import *
from mysql.connector import (connection)

cnx = connection.MySQLConnection(user=USER, password=PW,
                                    host=HOST, database=DB)

cnx.close()

