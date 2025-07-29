#!/usr/bin/python3
"""4.Cities by states"""

import MySQLdb
import sys


def filter_cities_by_state(username, password, database):
    """filtering cities by state, joining tables by state_id"""
    db_connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db_connect.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities INNER JOIN states "
        "ON cities.state_id = states.id "
        "ORDER BY cities.id ASC;"
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close
    db_connect.close


if __name__ == "__main__":
    """stops execute on import"""
    filter_cities_by_state(
        sys.argv[1], sys.argv[2], sys.argv[3])
