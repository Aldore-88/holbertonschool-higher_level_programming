#!/usr/bin/python3
"""4.Cities by states"""

import MySQLdb
import sys


def filter_by_state_argument(username, password, database, filter_by_state):
    """filtering cities by state, joining tables by state_id"""
    db_connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd="",
        db=database
    )

    cur = db_connect.cursor()
    cur.execute(
        "SELECT cities.name "
        "FROM states INNER JOIN cities "
        "ON states.id = cities.state_id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC;", (filter_by_state,)
    )

    rows = cur.fetchall()
    # print(len(rows))
    length = len(rows)
    i = 0
    while i < length:
        if i == length - 1:
            print(rows[i][0])
        else:
            print(rows[i][0], end=", ")
        i += 1

    cur.close
    db_connect.close


if __name__ == "__main__":
    """stops execute on import"""
    filter_by_state_argument(
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
