#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument and is safe from MySQL injections
"""
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3])
    cursor = database.cursor()
    search_term = sys.argv[4]
    cursor.execute("SELECT * FROM states WHERE BINARY name LIKE %s ORDER \
                   BY id;", (search_term,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    database.close()
