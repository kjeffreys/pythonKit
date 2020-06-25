from config import *
import mysql.connector
from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(user=USER, password=PW, host=HOST,
                                database=DB)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()

'''
if user is not provided...
Output: 
NameError: name 'USER' is not defined
'''

'''
if pw is not provided or user/pw pair is not correct...
Output: 
Something is wrong with your user name or password
'''

'''
elif err.errno == errorcode.ER_BAD_DB_ERROR:
Output: 
Database does not exist
'''



