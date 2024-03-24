#!/usr/bin/python3
"""
Scripts that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3])

    cursor = database.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
                   LEFT JOIN states ON cities.state_id = states.id ORDER BY \
                   cities.id ASC;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    database.close()
