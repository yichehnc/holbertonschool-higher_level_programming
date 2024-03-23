#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect
    database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY \
                   name LIKE 'N%' ORDER BY id;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    database.close()
