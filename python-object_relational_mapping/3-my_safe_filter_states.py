#!/usr/bin/python3
"""3.SQL Injection..."""

import MySQLdb
import sys

def safe_filter_by_user_input(username, password, database, input_filter):
    """stopping sql injection by using the %s parameter"""
    db_connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db_connect.cursor()
    cur.execute(
        "SELECT * FROM states "
        "WHERE name LIKE BINARY %s "
        "ORDER BY id ASC;", (input_filter,)
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    """stops execute on import"""
    safe_filter_by_user_input(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
