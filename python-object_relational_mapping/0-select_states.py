#!/usr/bin/python3
"""0.Get all states"""

import MySQLdb
import sys

def get_all_states(username, password, database):
    """connects to database and pulls all rows"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
        )

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()

if __name__ == "__main__":
    """stops from executing when imported"""
    get_all_states(sys.argv[1], sys.argv[2], sys.argv[3])