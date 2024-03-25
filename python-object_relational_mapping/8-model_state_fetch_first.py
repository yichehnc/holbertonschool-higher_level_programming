#!/usr/bin/python3
"""
Scripts that lists the first State objects from the database hbtn_0e_6_usa
"""
import MySQLdb
import sys
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id;")
    rows = cursor.fetchone()
    if rows:
        print("{}: {}".format(rows[0], rows[1]))
    else:
        print("Nothing")
    cursor.close()
    database.close()
