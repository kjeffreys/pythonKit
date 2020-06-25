import pandas as pd
import sqlite3

query = '''
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20),
 c REAL,        d INTEGER
);'''

data = [('Atlanta', 'Georgia', 1.25,  6),
        ('Tallahassee', 'Florida', 2.6, 3),
        ('Sacramento', 'California', 1.7, 5)]

sqliteDB = 'myDB.sqlite'

def basicConnect(query=query,db=sqliteDB):
    # connect with sqlite3 driver
    con = sqlite3.connect(db)

    # execute table create query
    con.execute(query)

    # commit change to myDB.sqlite
    con.commit()

def insertRecords(data=data,db=sqliteDB):
    # DML statement to insert records
    stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"

    # execute stmt
    con = sqlite3.connect(db)

    con.executemany(stmt, data)

    con.commit()

'''
Now to test if the records were entered correctly
'''
def selectAllRecords(db=sqliteDB):
    print("---selectAllRecords()---")
    con = sqlite3.connect(db)

    # most Python SQL drivers return a list of tuples when selecting data from a table
    cursor = con.execute('select * from test')

    # read the list of tuples returned into a native python list of tuples
    rows = cursor.fetchall()

    return rows

'''
You can pass the list of tuples returned from a python sql query
to the DataFrame constructor, but the columns names are also
required in the cursor's dsescription attribute.
'''
def showCursorDesc(db=sqliteDB):
    print("---showCursorDesc()---")
    con = sqlite3.connect(db)

    # most Python SQL drivers return a list of tuples when selecting data from a table
    cursor = con.execute('select * from test')

    return cursor.description

def constructDataFrame():
    print("---constructDataFrame()---")
    rows = selectAllRecords()
    columnNames = showCursorDesc()
    df = pd.DataFrame(rows, columns=[x[0] for x in columnNames])

    return df

if __name__ == "__main__":
    #basicConnect() # only do when creating new table
    #insertRecords() # only do when INSERT new rows
    print(selectAllRecords()) # expected: [('Atlanta', 'Georgia', 1.25, 6), ('Tallahassee', 'Florida', 2.6, 3), ('Sacramento', 'California', 1.7, 5)] # success!
    print(showCursorDesc())
    print(constructDataFrame())