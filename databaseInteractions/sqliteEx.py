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
    con = sqlite3.connect(db)

    # most Python SQL drivers return a list of tuples when selecting data from a table
    cursor = con.execute('select * from test')

    # read the list of tuples returned into a native python list of tuples
    rows = cursor.fetchall()

    return rows




if __name__ == "__main__":
    #basicConnect()
    insertRecords()
    print(selectAllRecords()) # expected: [('Atlanta', 'Georgia', 1.25, 6), ('Tallahassee', 'Florida', 2.6, 3), ('Sacramento', 'California', 1.7, 5)] # success!