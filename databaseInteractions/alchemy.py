'''
SQLAlchemy project is a popular Python SQL toolkit that abstracts away common differences
between SQL databases. panda.read_sql() is a function that enables reading data
from a general SQLAlchemy connection.
'''
import pandas as pd
import sqlalchemy as sqla
import sqlite3

engine = 'sqlite:///myAlchemyDB.sqlite'

def sqlAlchemyEngine(engine=engine):
    print("---createEngine()---")
    db = sqla.create_engine(engine)

    df = pd.read_sql('select * from test', db)
    
    return df

if __name__ == "__main__":
    print(sqlAlchemyEngine())