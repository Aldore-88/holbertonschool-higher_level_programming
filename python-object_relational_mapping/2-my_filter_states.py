#!/usr/bin/python3
"""2.Filter by user input"""
import MySQLdb
import sys


def filter_by_user_input(username, password, database, input_filter):
    """filter database by user input"""
    db_connect = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        port=3306,
        db=database
    )

    cur = db_connect.cursor()

    """
    can also use {0}
    LIKE BINARY for case senstitive
    """
    cur.execute(
        "SELECT * FROM states "
        "WHERE name LIKE BINARY '{}' "
        "ORDER BY id ASC;".format(input_filter)
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db_connect.close()


if __name__ == "__main__":
    """stops execute when imported"""
    filter_by_user_input(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
