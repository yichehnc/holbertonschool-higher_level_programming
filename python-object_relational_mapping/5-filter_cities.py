#!/usr/bin/python3
"""
Script that takes the name of a state as an argument and lists all cities of
that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3])
    cursor = database.cursor()
    search_term = sys.argv[4]
    cursor.execute("SELECT cities.name FROM cities LEFT JOIN states ON \
                   cities.state_id = states.id WHERE BINARY states.name \
                   LIKE %s ORDER BY cities.id ASC;", (search_term,))
    rows = cursor.fetchall()
    city_names = ', '.join(row[0] for row in rows)
    print(city_names)
    cursor.close()
    database.close()
