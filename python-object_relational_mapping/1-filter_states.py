#!/usr/bin/python3
"""1.Filter States"""

import MySQLdb
import sys


def filter_states_by_N(username, password, database):
    """filtering by states name starting with N"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()
    # SQL command - BINARY makes it case sensitive
    cur.execute("SELECT * FROM states "
                "WHERE name LIKE BINARY 'N%' ORDER BY id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    """stops execute when imported"""
    filter_states_by_N(sys.argv[1], sys.argv[2], sys.argv[3])
